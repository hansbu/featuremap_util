#!/usr/bin/env python
# Experimental.
import json
import os
import sys

import numpy as np
import pandas as pd
from sklearn import preprocessing


def prRed(skk): print("\033[91m {}\033[00m".format(skk))


def normalize(df, column_names_to_normalize):
    try:
        x = df[column_names_to_normalize].values  # returns a numpy array
        min_max_scaler = preprocessing.MinMaxScaler(feature_range=(0, 255))
        x_scaled = min_max_scaler.fit_transform(x)
        df_temp = pd.DataFrame(x_scaled, columns=column_names_to_normalize, index=df.index)
        df[column_names_to_normalize] = df_temp
    except ValueError as ex:
        prRed('FOUND NON-NUMERIC VALUES IN DATA COLUMNS')
        prRed(ex)
    return df


def get_meta(df):
    # Create first row JSON
    imw = df['image_width'].iloc[0]
    imh = df['image_height'].iloc[0]
    pw = df['patch_width'].iloc[0]
    ph = df['patch_height'].iloc[0]

    obj = {"img_width": str(imw),
           "img_height": str(imh),
           "patch_w": str(pw),
           "patch_h": str(ph),
           "png_w": str(np.ceil(imw / pw).astype(int)),
           "png_h": str(np.ceil(imh / ph).astype(int))}

    return obj


def get_columns(df):
    # Normalize to PNG dimensions
    df['i'] = df['patch_x'] / df['patch_width']
    df['j'] = df['patch_y'] / df['patch_height']

    # Round up
    df.i = np.ceil(df.i).astype(int)
    df.j = np.ceil(df.j).astype(int)

    to_be_removed = ['case_id', 'image_width', 'image_height', 'mpp_x', 'mpp_y', 'patch_x', 'patch_y', 'patch_width',
                     'patch_height', 'i', 'j']
    column_names_to_normalize = []
    cols = list(df.columns)
    column_names = ['i', 'j']
    for c in cols:
        if c not in to_be_removed:
            column_names.append(c)
            if c not in 'i' and c not in 'j':
                column_names_to_normalize.append(c)
    return column_names, column_names_to_normalize


def process(input, output):
    # Do for all files in directory:
    for filename in os.listdir(input):
        if filename.endswith(".csv"):
            fin = os.path.join(input, filename)
            df = pd.read_csv(fin)
            meta = get_meta(df)
            cols, column_names_to_normalize = get_columns(df)
            column_names = ",".join(cols)

            # Write first row JSON
            fout = os.path.join(output, filename)
            with open(fout, 'w') as f:
                f.write(json.dumps(meta) + '\n')
                f.write(column_names + '\n')

            df = df[cols]
            df = normalize(df, column_names_to_normalize)
            df = df.sort_values(['i', 'j'], ascending=[1, 1])

            with open(fout, 'a') as f:
                df.to_csv(f, mode='a', header=False, index=False)


if __name__ == "__main__":
    input = sys.argv[1]  # input
    output = sys.argv[2]  # output
    process(input, output)
