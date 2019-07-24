#!/usr/bin/env python
# Experimental.
import json
import os
import sys

import numpy as np
import pandas as pd


def normalize(df):
    result = df.copy()
    for feature_name in df.columns:
        max_value = df[feature_name].max()
        min_value = df[feature_name].min()
        result[feature_name] = (df[feature_name] - min_value) / (max_value - min_value)
    return result


def ordenar(df):
    # Sort
    result = df.copy()
    result = result.sort_values(['patch_x', 'patch_y'], ascending=[1, 1])
    # PNG i,j
    result['i'] = result['patch_x'] / df['patch_width']
    result['j'] = result['patch_y'] / df['patch_height']
    # Round up
    result.i = np.ceil(result.i).astype(int)
    result.j = np.ceil(result.j).astype(int)
    return result


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
    # Columns
    df['i'] = df['patch_x'] / df['patch_width']
    df['j'] = df['patch_y'] / df['patch_height']
    df.i = np.ceil(df.i).astype(int)
    df.j = np.ceil(df.j).astype(int)

    the_nope_list = ['case_id', 'image_width', 'image_height', 'mpp_x', 'mpp_y', 'patch_x', 'patch_y', 'patch_width',
                     'patch_height', 'i', 'j']
    cols = list(df.columns)
    cols1 = ['i', 'j']
    for c in cols:
        if c not in the_nope_list:
            cols1.append(c)
    return cols1


def check_csv(somefile):
    data = pd.DataFrame(somefile)
    cols = list(data.columns)
    print(f'{str(len(cols))} columns')


def process(input, output):
    # Do for all files in directory:
    for filename in os.listdir(input):
        if filename.endswith(".csv"):
            fin = os.path.join(input, filename)
            check_csv(fin)

            df = pd.read_csv(input)
            meta = get_meta(df)
            cols = get_columns(df)
            columns = ",".join(cols)

            # Write first row JSON
            fout = os.path.join(output, filename)
            with open(fout, 'w') as f:
                f.write(json.dumps(meta) + '\n')
                f.write(columns + '\n')

            ddf = ordenar(df)

            with open(output, 'a') as f:
                ddf.to_csv(f, mode='a', header=False, index=False)


if __name__ == "__main__":
    input = sys.argv[1]  # input
    output = sys.argv[2]  # output
    process(input, output)
