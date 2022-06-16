from sqlite3 import Date
import pandas as pd
from pyparsing import Regex


erhdatablecleaned = pd.read_csv('Merged_Tables/erhdatablecleaned6.16.22.csv')

#Merge columns 
erhdatablecleaned['Sender'] = erhdatablecleaned['W: Last'] + ", " + erhdatablecleaned['W: First']

erhdatablecleaned['Recipient'] = erhdatablecleaned['R: Last'] + ", " + erhdatablecleaned['R: First']

erhdatablecleaned['Sender Location'] = erhdatablecleaned['L: City'] + ", " + erhdatablecleaned['L: Country']

erhdatablecleaned['Recipient Location'] = erhdatablecleaned['R: City'] + ", " + erhdatablecleaned['R: Country']

#delete unnecessary columns
erhdatablecleaned.drop(['Item ID', 'W: First', 'W: Last', 'R: First', 'R: Last', 'L: Language', 'O/X/C/D', 'MS/TS', 'R: City', 'R: Country', 'L: Country', 'L: City'], axis=1, inplace=True) 

#change names of columns 
erhdatablecleaned.rename(columns={'L: Date': 'Date', 'Archive Location': 'Archive', 'Description': 'Comments'}, inplace=True)

#reorder columns 
erhdatablecleaned = erhdatablecleaned.reindex(columns=['File Name', 'Sender', 'Recipient', 'Date', 'Sender Location', 'Recipient Location', 'Archive', 'Rauner Item ID', 'Copyright Holder', 'Comments'])

#add columns 
erhdatablecleaned.insert(7, 'Published', '')

#convert column types 
erhdatablecleaned['Archive'] = erhdatablecleaned['Archive'].astype(str)

erhdatablecleaned['Copyright Holder'] = erhdatablecleaned['Copyright Holder'].astype(str)

#add DA to archive column
erhdatablecleaned = erhdatablecleaned.assign(Archive = 'ERHF Digital Archive' )

#replace NaN values 
erhdatablecleaned['Date'] = erhdatablecleaned['Date'].fillna(0)

#replace unknown values
erhdatablecleaned = erhdatablecleaned.replace({'Date': 'unknown'}, {'Date': ''})

#convert simple dates
erhdatablecleaned['Date'] = pd.to_datetime(erhdatablecleaned['Date'], errors='coerce')


#delete ALL duplicate rows 
#erhdatablecleaned.drop_duplicates(subset='Date', keep = 'first', inplace=True)

#Change index numbering 
erhdatablecleaned.index = range(len(erhdatablecleaned))

erhdatablecleaned.to_csv('test1.csv')
