import pandas as pd

#import digital archive ERH-FR 1914 DA CSV File 
df2 = pd.read_csv('Tables/ERHDA Rosenzweig Correspondence.csv')

#Merge columns 
df2['Sender'] = df2['W: Last'] + ", " + df2['W: First']

df2['Recipient'] = df2['R: Last'] + ", " + df2['R: First']

df2['Sender Location'] = df2['L: City'] + ", " + df2['L: Country']

df2['Recipient Location'] = df2['R: City'] + ", " + df2['R: Country']

#delete unnecessary columns
df2.drop(['Item ID', 'File Name', 'W: First', 'W: Last', 'R: First', 'R: Last', 'L: Language', 'O/C/D/X', 'MS/TS/P', 'ERH', 'pages', 'MRH', 'pages.1', 'Other 1', 'Other 2', 'Other 3', 'To Others', 'pages.2', 'Total L', 'Total p', 'Enclosures', 'Note1', 'Note2', 'URLw/Bio,etc', 'R: City', 'R: Country', 'L: Country', 'L: City'], axis=1, inplace=True) 

#change names of columns 
df2.rename(columns={'L: Date': 'Date', 'Archive Location': 'Archive', 'Description': 'Comments',}, inplace=True)


#reorder columns 
df2 = df2.reindex(columns=['Sender', 'Recipient', 'Date', 'Sender Location', 'Recipient Location', 'Archive', 'Rauner Item ID', 'Copyright Holder', 'Comments'])

#add columns 
df2.insert(7, 'Published', '')

for col in df2.columns: 
    print(col)

#delete unnecessary rows (pages) 
#recognfigure date format to make it align with Kassel_Archive_table.py

print(df2.head(5))
