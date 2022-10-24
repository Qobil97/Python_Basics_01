import os


from openpyxl import load_workbook

wb = load_workbook(filename='combined_raw_materials.xlsx', data_only=True)



import pandas as pd

df=pd.read_excel('combined_raw_materials.xlsx')




#print(df['supplier name'])
# df['flag'] = 1
# print(df)


# dups = df.groupby(df.columns.tolist()).size().reset_index().rename(columns={0: 'count'})
# dups['count'].sum() - dups.shape[0]

#df.groupby(df.columns.tolist(), as_index=False).size()