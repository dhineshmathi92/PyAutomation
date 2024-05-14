import os
import pandas as pd

# File path assignment and reading file of any format

filepath=r'D:\Pythonprojects\Jsonsources'

for filename in os.listdir(filepath):  # iterates through the different files in the mentioned location
    
    if filename.endswith('source.xlsx'):  # if file ends with 'source.xlsx' then that file is read into dataframe df1
        
        df1=pd.read_excel(filepath +'\\'+ filename)
        
    elif filename.endswith('target.xlsx'): # if file ends with 'target.xlsx' then that file is read into dataframe df2
        
        df2=pd.read_excel(filepath + '\\' + filename)
        
    elif filename.endswith('source.json'):
        
        df1 = pd.read_json (filepath + '\\' + filename)
        
    elif filename.endswith ('target.json'):
        
        df2 = pd.read_json (filepath + '\\' + filename)
        
    else:
        
        print('No valid files to read')

# Creating DataFrame 1 or reading through any sources

# df1 = pd.DataFrame({
#     'Date':['2013-11-24', '2013-11-24', '2013-11-24', '2013-11-24'],
#     'Fruit':['Banana', 'Orange', 'Apple', 'Celery'],
#     'Num':['22.1', '8.6', '7.6', '10.2'],
#     'Color':['Yellow', 'Orange', 'Green', 'Green']
#             })

#df1 = pd.read_excel('Students_DB01.xlsx')

# Creating DataFrame 2 or reading through any sources

# df2 = pd.DataFrame({
#     'Date':['2013-11-24', '2013-11-24', '2013-11-24', '2013-11-24', '2013-11-25', '2013-11-25'],
#     'Fruit':['Banana', 'Orange', 'Apple', 'Celery', 'Apple', 'Orange'],
#     'Num':['22.1', '8.6', '7.6', '10.2', '22.1', '8.6'],
#     'Color':['Yellow', 'Orange', 'Green', 'Green', 'Red', 'Orange']
#             })


#df2 = pd.read_excel('Students_DB02.xlsx')

# To find the symmetric difference, we concatenate the dataframes
# Concatenating both DataFrames
df = pd.concat([df1,df2])
df.reset_index(drop=True,inplace=True)

# Grouping based on the list of columns in df, to find the unique records
df_gpby=df.groupby(list(df.columns))

# Getting the indices of records that do not have matching records
idx=[x[0] for x in df_gpby.groups.values() if len(x)==1]

# Fetching the mismatch entries from 'df' with the list of indices 'idx'
mismatch_records=df.iloc[idx]
# df.reindex(idx)  -- another method of fetching the mismatch records

mismatch_records.to_excel(filepath+ '\\'+'Mismatch_records.xlsx',index=False)