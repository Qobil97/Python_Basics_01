import pandas as pd

df = pd.read_excel('combined_raw_materials.xlsx')
df['kichik harflik']=df['supplier name'].str.title()
#.str.lower() bu method hisoblandi-hammasi kichik, string.title() - every first letter is capital - camel case
print(df)