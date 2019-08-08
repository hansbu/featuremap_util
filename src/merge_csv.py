import pandas as pd

df1 = pd.read_csv('one.csv', delimiter=',')
df2 = pd.read_csv('two.csv', delimiter=',')
merged_df = df1.merge(df2, how='left', on=['i', 'j'])
# print(merged_df)
merged_df.fillna(0, inplace=True)
header = ["i", "j", "TIL_y", "Cancer", "Tissue"]
# merged_df.to_csv('output.csv', columns=header)
merged_df.to_csv('output.csv', columns=header, index=False)
