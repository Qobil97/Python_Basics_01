import pandas as pd

df = pd.read_excel('combined_raw_materials.xlsx')


df = df[df['supplier name'].str.contains('CASEA GMBH', na=False)]
#na is used to avoid this error: Cannot mask with non-boolean array containing NA / NaN values
print(df)