import pandas as pd

#import data 
df = pd.read_csv('Tables/tabula-DierichsTeilnachlassRosenzweig.csv')

#Rename columms in data set 
df.rename(columns={'Unnamed: 0': 'ID Num', 'Unnamed: 1': 'Box', 'Unnamed: 2': 'Format', 'Unnamed: 3': 'Style', 'Unnamed: 4': 'Sender', 'Unnamed: 5': 'Recipient', 'Unnamed: 6': 'Date', 'Unnamed: 7': 'Sender Location', 'Unnamed: 8': 'Published?', 'Unnamed: 9': 'GB?', 'Unnamed: 10': 'Comments', 'Unnamed: 11': '?', 'Unnamed: 12': '??'}, inplace=True)

#Delete unnecessary columns 
df.drop(['ID Num', 'Box', 'Format', 'Style', '?', '??'], axis=1, inplace=True)

#Delete unnecessary rows 
df.drop(index=df.index[0:2], axis=0, inplace=True)

#Change index numbering 
df.index = range(len(df))

#Print new data set
print(df.head(5))
