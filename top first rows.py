import pandas as pd

df = pd.read_excel('combined_raw_materials.xlsx')

important_rows=df.tail(20)
#-20 means here, from the bottom 20 rows. 20 ta degani noldan 19 gacha
print(important_rows)