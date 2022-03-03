import pandas as pd

from Kassel_Archive_Table import df
from ERHF_DArchive_TableEF1914 import df2

#merge databases together to create one database

NTTable = df.merge(df2, how='outer')

#reorder by date 
NTTable = NTTable.sort_values(by='Date')

#Change index numbering 
NTTable.index = range(len(NTTable))


NTTable.to_csv('NTTable1.csv', index = False)


 