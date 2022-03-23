import pandas as pd
import numpy as np

from Kassel_Archive_Table import df
from ERHF_DArchive_TableEF1914 import df2

#merge databases together to create one database

NTTable = df.merge(df2, how='outer')

#reorder by date 
NTTable = NTTable.sort_values(by='Date')

#change index numbering 
NTTable.index = range(len(NTTable))

#check how many records are in the dataset 
NTTable.info()

#count number of unique senders in dataset
Sender_Count = NTTable['Sender'].value_counts().head(10)

print(Sender_Count)

#Count number of unique recipients in dataset 
Recipient_Count = NTTable['Recipient'].value_counts().head(10)

print(Recipient_Count)

NTTable.groupby(['Recipient'])['Recipient'].count().columns
