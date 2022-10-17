import pandas as pd

mbcc_data = 'combined_raw_materials.xlsx'

df = pd.DataFrame(mbcc_data, index=pd.Index(name='supplier code'), coulmns=pd.Index(["supplier code", "BI number", "Raw material description SAP	Supplier/Other material name", "supplier name"]), name="supplier code"))

pd.read_excel('combined_raw_materials.xlsx')
unique = mbcc_data.column_name.unique()
print(df)

print("number of duplicate rows is:", duplicates)
