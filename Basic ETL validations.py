import pandas as pd
import numpy as np

df1 = pd.DataFrame({'Name':['Dhinesh','Jayakumar','Geetha'], 'Age':[27, 25, 23]})
df2 = pd.DataFrame({'Name':['Mathiyalagan', 'Jayalakshmi', 'Dhinesh', 'Jayakumar'], 'Age':[55, 43, 27, 25], 
                    'Occupation':['Dailywork', 'Home maker', 'IT', 'IT']})

df2.reset_index(inplace=True)


df1.reset_index(inplace=True)

# Count validation
print('Number of records in df1: ',df1['index'].count())
print('Number of records in df2: ',df2['index'].count())
print('Count Matching ?: ' ,df1['index'].count() == df2['index'].count()) # comparing the count of primary keys in both dataframes.



# Duplicate Validation

# Adding duplicate records in both df1 and df2

new_rows_df1 = pd.DataFrame({'index': [0, 2, 5], 'Name': ['Dhinesh', 'Geetha', 'Nithi'], 'Age': [27, 23, 30]})
new_rows_df2 = pd.DataFrame({'index': [0, 1], 'Name': ['Mathiyalagan', 'Jayalakshmi'], 'Age': [55, 43],
                            'Occupation':['Dailywork', 'Home maker']})

df1_dups= pd.concat([df1, new_rows_df1])
df1_dups.reset_index(drop=True, inplace=True)

df2_dups= pd.concat([df2, new_rows_df2])
df2_dups.reset_index(drop=True, inplace=True)

# Finding duplicates in df1_dups
print('Duplicates in Dataframe 1')
print(df1_dups[df1_dups.duplicated(subset=df1_dups.columns)])

# Finding duplicates in df2_dups
print('\n\n')

print('Duplicates in Dataframe 2')
print(df2_dups[df2_dups.duplicated(subset=df2_dups.columns)])


# Removing duplicates from df1_dups
df1_dups.drop_duplicates(subset=df1_dups.columns, keep='first', inplace=True)

# Removing duplicates from df2_dups
df2_dups.drop_duplicates(subset=df2_dups.columns, keep='first', inplace=True)

print('\n')
print('After removing duplicates from both dataframes',end='\n\n')

print(df1_dups)
print('\n')
print(df2_dups)




# Check for new row addition by comparing two dataframes

# Creating new dataframe consisting of df1 + new records

new_records=pd.DataFrame({'index':[3, 4], 'Name':['Mathiyalagan', 'Jayalakshmi'], 'Age':[55, 43]})
df3= pd.concat([df1, new_records])
df3.reset_index(drop=True, inplace=True)

# Find new records addition in df3

# 1. concat two dataframes
df_concat= pd.concat([df1, df3])
df_concat.reset_index(drop=True, inplace=True)

# groupby list of columns in concatenated dataframe df_concat
grp_df=df_concat.groupby(by=list(df_concat.columns))

# Identifying the indices of new columns
indx = [i[0] for i in grp_df.groups.values() if len(i)==1]

print('New records are : ')
print(df_concat.iloc[indx])


# Check if any existing record is modified.

# To check if the record's modified, two dataframes should have same primary keys for the records.

# numpy module is required check the where function.

# Copying df2 data into df4 

df4=df2.copy()

# modifying the df4 data

df4['Occupation'].loc[0] ='Daily wages'
df4['Occupation'].iloc[2] = 'IT-QA'
df4['Occupation'].loc[3]='IT-Dev'

# identifying the value change in a column using np.where() function
df4['value_change?'] = np.where(df2['Occupation']!=df4['Occupation'],df2['Occupation']+'-->'+df4['Occupation'] ,False)

print(df4)


# Check if any old record is deleted

# Deleting some old records from df2 and creating a new dataframe df_oldel

df_oldel=df2.copy()

# deleting two rows from a dataframe
df_oldel.drop(df_oldel.index[[1,3]],inplace=True)

# comparing two dataframes for record deletion
#method 1
#df2[df2.merge(df_oldel,how='outer',indicator=True)['_merge']=='left_only']

#method 2
print('Deleted old records are:')
print(df2[df2.merge(df_oldel,how='outer',indicator=True).loc[:,'_merge']=='left_only'])

    
	
	