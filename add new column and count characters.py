import pandas as pd

df = pd.read_excel('combined_raw_materials.xlsx')
df['yangi ustun'] = df['Supplier/Other material name'].str.len()
# a new column called - yangi ustun
print(df)
