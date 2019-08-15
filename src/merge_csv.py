import sys

import pandas as pd


def wip():
    c1 = str(sys.argv[1])
    c2 = str(sys.argv[2])
    df1 = pd.read_csv(c1, delimiter=',')
    df2 = pd.read_csv(c2, delimiter=',')

    merged_df = df1.merge(df2, how='left', on=['i', 'j'])
    # print(merged_df)
    merged_df.fillna(0, inplace=True)
    # header = ["i", "j", "TIL_y", "Cancer", "Tissue"]
    # merged_df.to_csv('merged.csv', columns=header)
    # merged_df.to_csv('merged.csv', columns=header, index=False)
    merged_df.to_csv('merged.csv')


wip()


def original():
    df1 = pd.read_csv('one.csv', delimiter=',')
    df2 = pd.read_csv('two.csv', delimiter=',')
    merged_df = df1.merge(df2, how='left', on=['i', 'j'])
    # print(merged_df)
    merged_df.fillna(0, inplace=True)
    header = ["i", "j", "TIL_y", "Cancer", "Tissue"]
    # merged_df.to_csv('merged.csv', columns=header)
    merged_df.to_csv('merged.csv', columns=header, index=False)
