import pandas as pd

#import data 
df = pd.read_csv('Kassel_Tables/tabula-DierichsTeilnachlassRosenzweig1.csv')

#Rename columms in data set 
df.rename(columns={'Unnamed: 0': 'ID Num', 'Unnamed: 1': 'Box', 'Unnamed: 2': 'Format', 'Unnamed: 3': 'Style', 'Unnamed: 4': 'Sender', 'Unnamed: 5': 'Recipient', 'Unnamed: 6': 'Date', 'Unnamed: 7': 'Sender City', 'Unnamed: 8': 'Published?', 'Unnamed: 9': 'GB?', 'Unnamed: 10': 'Comments', 'Unnamed: 11': '?', 'Unnamed: 12': '??'}, inplace=True)

#merge columns 
df['Published'] = df['Published?'] + df['GB?']

#Delete unnecessary columns 
df.drop(['ID Num', 'Box', 'Format', 'Style', '?', '??', 'Published?', 'GB?'], axis=1, inplace=True)

#add columns 
df.insert(3, 'Sender Country', '')

df.insert(4, 'Recipient City', '')

df.insert(5, 'Recipient Country', '')

df.insert(6, 'Archive', '')

df.insert(7, 'Rauner Item ID', '')

df.insert(8, 'Copyright Holder', '')

#reorder columns
df = df.reindex(columns=['Sender', 'Recipient', 'Date', 'Sender City', 'Sender Country', 'Recipient City', 'Recipient Country', 'Archive', 'Rauner Item ID',  'Published', 'Copyright Holder', 'Comments'])

#add Kassel to archive column
df = df.assign(Archive = 'Kassel')

#delete unnecessary rows (use for function)
df.drop(index=df.index[0:2], axis=0, inplace=True)

#Change index numbering 
df.index = range(len(df))

#Replace NaN values 
df['Date'] = df['Date'].fillna(0)

#Converting integers to datetime format
df['Date'] = pd.to_datetime(df['Date'], errors='coerce')

#Export to CV
#df.to_csv('Kassel Corrected Spreadsheet 6.22.22.csv')




