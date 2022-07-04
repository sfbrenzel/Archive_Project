import pandas as pd
import numpy as np

pd.read_csv('Merged_Tables/ERHFDA Cleaned 6.22.22.csv')
pd.read_csv('Merged_Tables/Kassel Cleaned 6.22.22.csv')

#merge databases together to create one database (stretch feature list)

erhdf1 = pd.read_csv('Merged_Tables/ERHFDA Cleaned 6.22.22.csv')
kasseldf1 = pd.read_csv('Merged_Tables/Kassel Cleaned 6.22.22.csv')
NTTable = pd.concat([erhdf1, kasseldf1])

#add columns
NTTable.insert(6, 'Latitude', '')
NTTable.insert(7, 'Longitude', '')

#change index numbering 
NTTable.index = range(len(NTTable))


#check how many records are in the dataset 
#NTTable.info()

#count number of unique senders in dataset
#Sender_Count = NTTable['Sender'].value_counts().head(10)

#print(Sender_Count)

#Count number of unique recipients in dataset 
#Recipient_Count = NTTable['Recipient'].value_counts().head(10)

#print(Recipient_Count)

#drop first column 
NTTable.drop(['Unnamed: 0'], axis=1, inplace=True) 

#drop index 
NTTable.set_index('Sender', inplace=True)

#sort by sender 
NTTable.sort_values('Sender', inplace=True)

#Export to CV
NTTable.to_csv('tableautest.csv')

