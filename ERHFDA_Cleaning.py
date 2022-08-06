from sqlite3 import Date
import pandas as pd
import numpy as np
from pyparsing import Regex


erhdatablecleaned = pd.read_csv('Merged_Tables/ERHFDA MERGED 8.05.22.csv')

#Merge columns 
erhdatablecleaned['Sender'] = erhdatablecleaned['W: Last'] + ", " + erhdatablecleaned['W: First']

erhdatablecleaned['Recipient'] = erhdatablecleaned['R: Last'] + ", " + erhdatablecleaned['R: First']

#delete unnecessary columns
erhdatablecleaned.drop(['Unnamed: 0', 'Location', 'Item ID', 'W: First', 'W: Last', 'R: First', 'R: Last', 'L: Language', 'O/X/C/D', 'O/C/D/X', 'MS/TS/P', 'MS/TS', 'ERH', 'pages', 'MRH', 'pages.1', 'Other 1', 'Other 2', 'Other 3', 'To Others', 'pages.2', 'Total L', 'Total p', 'Enclosures', 'Note1', 'Note2', 'URLw/Bio,etc', 'Archive ID', 'Unnamed: 32', 'Copyright Holder.1', 'Copyright Holder.2', 'Unnamed: 34', 'Unnamed: 35', 'Unnamed: 33', 'Unnamed: 36', 'Unnamed: 37', 'Unnamed: 38', 'Unnamed: 39', 'Unnamed: 40', 'Unnamed: 41', 'Unnamed: 42', 'Unnamed: 43', 'Unnamed: 44', 'Unnamed: 45', 'Unnamed: 46', 'Unnamed: 47', 'Unnamed: 48', 'Unnamed: 49', 'Unnamed: 50', 'Unnamed: 51', 'Unnamed: 52', 'Unnamed: 53', 'Unnamed: 54', 'Unnamed: 55', 'Unnamed: 56', 'Unnamed: 57', 'Unnamed: 58', 'Unnamed: 59', 'Unnamed: 60', 'Unnamed: 61', 'Unnamed: 62', 'Unnamed: 63', 'Unnamed: 64', 'Unnamed: 65', 'Unnamed: 66', 'Unnamed: 67', 'Unnamed: 68', 'Unnamed: 69', 'Unnamed: 70', 'Unnamed: 71', 'Unnamed: 72', 'Unnamed: 73', 'Unnamed: 74', 'Unnamed: 75', 'Unnamed: 76', 'Unnamed: 77', 'Unnamed: 78', 'Unnamed: 79', 'Unnamed: 80', 'Unnamed: 81', 'Unnamed: 82', 'Unnamed: 83', 'Unnamed: 84', 'Unnamed: 85', 'Unnamed: 86', 'Unnamed: 87', 'Unnamed: 88', 'Unnamed: 89', 'Unnamed: 90', 'Unnamed: 91', 'Unnamed: 92', 'Unnamed: 93', 'Unnamed: 94', 'Unnamed: 95', 'Unnamed: 96', 'Unnamed: 97', 'Unnamed: 98', 'Unnamed: 99', 'Unnamed: 100', 'Unnamed: 101', 'Unnamed: 102', 'Unnamed: 103', 'Unnamed: 104', 'Unnamed: 105', 'Unnamed: 106', 'Unnamed: 107', 'Unnamed: 108', 'Unnamed: 109', 'Unnamed: 110', 'Unnamed: 111', 'Unnamed: 112', 'Unnamed: 113', 'Unnamed: 114', 'Unnamed: 115', 'Unnamed: 116', 'Unnamed: 117', 'Unnamed: 118', 'Unnamed: 119', 'Unnamed: 120', 'Unnamed: 121', 'Unnamed: 122', 'Unnamed: 123', 'Unnamed: 124', 'Unnamed: 125', 'Unnamed: 126', 'Unnamed: 127', 'Unnamed: 128', 'Unnamed: 129', 'Unnamed: 130', 'Unnamed: 131', 'Unnamed: 132', 'Unnamed: 133', 'Unnamed: 134', 'Unnamed: 135', 'Unnamed: 136', 'Unnamed: 137', 'Unnamed: 138', 'Unnamed: 139', 'Unnamed: 140', 'Unnamed: 141', 'Unnamed: 142', 'Unnamed: 143', 'Unnamed: 144', 'Unnamed: 145', 'Unnamed: 146', 'Unnamed: 147', 'Unnamed: 148', 'Unnamed: 149', 'Unnamed: 150', 'Unnamed: 151', 'Unnamed: 152', 'Unnamed: 153', 'Unnamed: 154', 'Unnamed: 155', 'Unnamed: 156', 'Unnamed: 157', 'Unnamed: 158', 'Unnamed: 159', 'Unnamed: 160', 'Unnamed: 161', 'Unnamed: 162', 'Unnamed: 163', 'Unnamed: 164', 'Unnamed: 165', 'Unnamed: 166', 'Unnamed: 167', 'Unnamed: 168', 'Unnamed: 169', 'Unnamed: 170', 'Unnamed: 171', 'Unnamed: 172', 'Unnamed: 173', 'Unnamed: 174', 'Unnamed: 175', 'Unnamed: 176', 'Unnamed: 177', 'Unnamed: 178', 'Unnamed: 179', 'Unnamed: 180', 'Unnamed: 181', 'Unnamed: 182', 'Unnamed: 183', 'Unnamed: 184', 'Unnamed: 185', 'Unnamed: 186', 'Unnamed: 187', 'Unnamed: 188', 'Unnamed: 189', 'Unnamed: 190', 'Unnamed: 191', 'Unnamed: 192', 'Unnamed: 193', 'Unnamed: 194', 'Unnamed: 195', 'Unnamed: 196', 'Unnamed: 197', 'Unnamed: 198', 'Unnamed: 199', 'Unnamed: 200', 'Unnamed: 201', 'Unnamed: 202', 'Unnamed: 203', 'Unnamed: 204', 'Unnamed: 205', 'Unnamed: 206', 'Unnamed: 207', 'Unnamed: 208', 'Unnamed: 209', 'Unnamed: 210', 'Unnamed: 211', 'Unnamed: 212', 'Unnamed: 213', 'Unnamed: 214', 'Unnamed: 215', 'Unnamed: 216', 'Unnamed: 217', 'Unnamed: 218', 'Unnamed: 219', 'Unnamed: 220', 'Unnamed: 221', 'Unnamed: 222', 'Unnamed: 223', 'Unnamed: 224', 'Unnamed: 225', 'Unnamed: 226', 'Unnamed: 227', 'Unnamed: 228', 'Unnamed: 229', 'Unnamed: 230', 'Unnamed: 231', 'Unnamed: 232', 'Unnamed: 233', 'Unnamed: 234', 'Unnamed: 235', 'Unnamed: 236', 'Unnamed: 237', 'Unnamed: 238', 'Unnamed: 239', 'Unnamed: 240', 'Unnamed: 241', 'Unnamed: 242', 'Unnamed: 243', 'Unnamed: 244', 'Unnamed: 245', 'Unnamed: 246', 'Unnamed: 247', 'Unnamed: 248', 'Unnamed: 249', 'Unnamed: 250', 'Unnamed: 251', 'Unnamed: 252', 'Unnamed: 253', 'Unnamed: 254', 'Unnamed: 255', 'Note 1', 'MRH-a', 'HCG', 'RHG', 'Others', ' Item ID', 'ERH.1', 'HRH', 'Pages', 'Pages.1', 'Pages.2', 'Total P', 'Running L', 'Running p', 'Wacke'], inplace=True, axis=1) 

#change names of columns 
erhdatablecleaned.rename(columns={'L: Date': 'Date', 'Archive Location': 'Archive', 'Description': 'Comments', 'L: City': 'Sender City', 'L: Country': 'Sender Country', 'R: City': 'Recipient City', 'R: Country': 'Recipient Country'}, inplace=True)

#add columns 
erhdatablecleaned.insert(8, 'Published', '')

#Fixing Value Error Bug: Unique Index Values
#print(erhdatablecleaned.index.is_unique)
#print(erhdatablecleaned.index.duplicated())

#split columns 
erhdatablecleaned = erhdatablecleaned['File Name'].str.rsplit('-',1, expand=True).add_prefix('test').join(erhdatablecleaned)

#convert column types 
erhdatablecleaned['Archive'] = erhdatablecleaned['Archive'].astype(str)

erhdatablecleaned['Copyright Holder'] = erhdatablecleaned['Copyright Holder'].astype(str)

#add DA to archive column
erhdatablecleaned = erhdatablecleaned.assign(Archive = 'ERHF Digital Archive' )

#convert simple dates
erhdatablecleaned['Date'] = pd.to_datetime(erhdatablecleaned['Date'], errors='coerce')

#convert date format 
erhdatablecleaned['Date'] = pd.to_datetime(erhdatablecleaned['Date'], format='%Y-%m-%d')

#drop hours
erhdatablecleaned['Date'] = pd.to_datetime(erhdatablecleaned['Date']).dt.date

#replace blank values
erhdatablecleaned['Date'] = erhdatablecleaned['Date'].fillna('NA')

#delete ALL duplicate rows (still getting rid of non duplicates, need to figure out) 
erhdatablecleaned.drop_duplicates(subset=['test0'], keep = 'first', inplace=True)

#drop third set of columns 
erhdatablecleaned.drop(['File Name','test0', 'test1'], axis=1, inplace=True) 

#Change index numbering 
erhdatablecleaned.index = range(len(erhdatablecleaned))

#reorder columns 
erhdatablecleaned = erhdatablecleaned.loc[:, ['Sender', 'Recipient', 'Date', 'Sender City', 'Sender Country', 'Recipient City', 'Recipient Country', 'Archive', 'Rauner Item ID', 'Copyright Holder', 'Comments']]

#export to csv
erhdatablecleaned.to_csv('ERHFDA CLEANED 8.05.22.csv')
