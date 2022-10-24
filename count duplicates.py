import pandas as pd
import numpy as np

df = pd.read_excel('combined_raw_materials.xlsx')

df1 = df['supplier name']

given_data=np.where(df1=='AL RAMA INTERNATIONAL',1,0)
 for items in given_data:
     give==+1
print(sum(given_data))
#      break

#print(df.groupby(['supplier name'])['supplier name'].count())
#print(df1)






# df2=df1[arr_index]
# str_count1=df2.count(1)
# print ("The count of '1' is", str_count1)
 