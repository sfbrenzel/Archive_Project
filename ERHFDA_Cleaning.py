from sqlite3 import Date
import pandas as pd
from pyparsing import Regex


erhdatablecleaned = pd.read_csv('Merged_Tables/erhdatablemerged6.16.22.csv')

#Merge columns 
erhdatablecleaned['Sender'] = erhdatablecleaned['W: Last'] + ", " + erhdatablecleaned['W: First']

erhdatablecleaned['Recipient'] = erhdatablecleaned['R: Last'] + ", " + erhdatablecleaned['R: First']

#delete unnecessary columns
erhdatablecleaned.drop(['Item ID', 'W: First', 'W: Last', 'R: First', 'R: Last', 'L: Language', 'O/X/C/D', 'MS/TS'], axis=1, inplace=True) 

#change names of columns 
erhdatablecleaned.rename(columns={'L: Date': 'Date', 'Archive Location': 'Archive', 'Description': 'Comments', 'L: City': 'Sender City', 'L: Country': 'Sender Country', 'R: City': 'Recipient City', 'R: Country': 'Recpient Country' }, inplace=True)

#reorder columns 
erhdatablecleaned = erhdatablecleaned.reindex(columns=['File Name', 'Sender', 'Recipient', 'Date', 'Sender City', 'Sender Country', 'Recipient City', 'Recipient Country', 'Archive', 'Rauner Item ID', 'Copyright Holder', 'Comments'])

#add columns 
erhdatablecleaned.insert(8, 'Published', '')

#split columns 
erhdatablecleaned = erhdatablecleaned['File Name'].str.rsplit('-',1, expand=True).add_prefix('test').join(erhdatablecleaned)

#drop second set of columns
erhdatablecleaned.drop(['File Name', 'test1'], axis=1, inplace=True)

#convert column types 
erhdatablecleaned['Archive'] = erhdatablecleaned['Archive'].astype(str)

erhdatablecleaned['Copyright Holder'] = erhdatablecleaned['Copyright Holder'].astype(str)

#add DA to archive column
erhdatablecleaned = erhdatablecleaned.assign(Archive = 'ERHF Digital Archive' )

#replace NaN values 
erhdatablecleaned['Date'] = erhdatablecleaned['Date'].fillna(0)

#convert simple dates
erhdatablecleaned['Date'] = pd.to_datetime(erhdatablecleaned['Date'], errors='coerce')

#convert date format 
erhdatablecleaned['Date'] = pd.to_datetime(erhdatablecleaned['Date'], format='%Y-%M-%D')

#replace blank values
erhdatablecleaned = erhdatablecleaned.replace({'Date': ''}, {'Date': '0000-00-00'})


#delete ALL duplicate rows (still getting rid of non duplicates, need to figure out) 
erhdatablecleaned.drop_duplicates(subset=['test0'], keep = 'first', inplace=True)

#Change index numbering 
erhdatablecleaned.index = range(len(erhdatablecleaned))

#drop third set of columns 
erhdatablecleaned.drop(['test0'], axis=1, inplace=True) 

#export to csv
erhdatablecleaned.to_csv('ERHFDA Cleaned 6.22.22.csv')
