import pandas as pd
from ERHFDA_Merge import erhdatable

#import digital archive ERH-FR 1914 DA CSV File 
df2 = erhdatable

#Merge columns 
df2['Sender'] = df2['W: Last'] + ", " + df2['W: First']

df2['Recipient'] = df2['R: Last'] + ", " + df2['R: First']

df2['Sender Location'] = df2['L: City'] + ", " + df2['L: Country']

df2['Recipient Location'] = df2['R: City'] + ", " + df2['R: Country']

#delete unnecessary columns
df2.drop(['Item ID', 'File Name', 'W: First', 'W: Last', 'R: First', 'R: Last', 'L: Language', 'O/C/D/X', 'MS/TS/P', 'ERH', 'pages', 'MRH', 'pages.1', 'Other 1', 'Other 2', 'Other 3', 'To Others', 'pages.2', 'Total L', 'Total p', 'Enclosures', 'Note1', 'Note2', 'URLw/Bio,etc', 'R: City', 'R: Country', 'L: Country', 'L: City'], axis=1, inplace=True) 

#change names of columns 
df2.rename(columns={'L: Date': 'Date', 'Archive Location': 'Archive', 'Description': 'Comments'})

#reorder columns 
df2 = df2.reindex(columns=['Sender', 'Recipient', 'Date', 'Sender Location', 'Recipient Location', 'Archive', 'Rauner Item ID', 'Copyright Holder', 'Comments'])

#add columns 
df2.insert(7, 'Published', '')

#convert column types 
df2['Archive'] = df2['Archive'].astype(str)

df2['Copyright Holder'] = df2['Copyright Holder'].astype(str)

#add DA to archive column
df2 = df2.assign(Archive = 'ERHF Digital Archive' )

#Replace NaN values 
df2['Date'] = df2['Date'].fillna(0)

#recognfigure date format
df2['Date'] = pd.to_datetime(df2['Date'], errors='coerce')

#delete empty rows 
df2.drop(index=df2.index[13:22], axis=0)

#delete ALL duplicate rows 
df2.drop_duplicates(subset='Date', keep = 'first')

#Change index numbering 
df2.index = range(len(df2))


df2.to_csv('test1.csv')
