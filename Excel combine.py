import glob
import pandas as pd

path = "C:/Users/HP/OneDrive/self learn/Python/MBCC/work/files"
file_list = glob.glob(path + "/*.xlsx")


excl_list = []

for file in file_list:
    excl_list.append(pd.read_excel(file))

# create a new dataframe to store the
# merged excel file.
excl_merged = pd.DataFrame()

for excl_new_file in excl_list:


    excl_merged = excl_merged.append(
        excl_new_file, ignore_index=True)


excl_merged.to_excel('combined_raw_materials.xlsx', index=False)
