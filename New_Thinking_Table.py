import pandas as pd
import numpy as np

pd.read_csv('Cleaned_Tables/ERHFDA Cleaned 8.05.22.csv')
pd.read_csv('Cleaned_Tables/Kassel Cleaned 6.22.22.csv')

#merge databases together to create one database (stretch feature list)

erhdf1 = pd.read_csv('Cleaned_Tables/ERHFDA Cleaned 8.05.22.csv')
kasseldf1 = pd.read_csv('Cleaned_Tables/Kassel Cleaned 6.22.22.csv')
NTTable = pd.concat([erhdf1, kasseldf1])

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

#drop columns 
NTTable.drop(['Unnamed: 0', 'Archive.1', 'Rauner Item ID'], axis=1, inplace=True) 

#add columns
NTTable.insert(8, 'Duplicates?', '')
NTTable.insert(10, 'Transcribed', '')
NTTable.insert(11, 'Transcription Link', '')

#drop index 
NTTable.set_index('Sender', inplace=True)

#sort by sender 
NTTable.sort_values('Sender', inplace=True)

#Export to CV
NTTable.to_csv('combinedarchives.csv')

