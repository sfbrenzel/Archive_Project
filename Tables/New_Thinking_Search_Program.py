import pandas as pd  
from tabulate import tabulate 

#import data for data search 
tdb = pd.read_csv('Tables/NTTable.csv')


option_table = {1: 'Sender', 2: 'Recipient', 3: 'Date', 4: 'Archive'}

#define search options
def search(field):
    search_q = input(f"Please enter {field}: ")
    search_a = tdb.loc[tdb[field] == search_q]
    if len(search_a) > 0: 
        print(tabulate(search_a, headers='firstrow', tablefmt='fancy_grid'))
    else: 
        print(f'{field} not found in database')

#main menu of search options
def menu(): 
    print('[1] Sender: Last, First')
    print('[2] Recipient: Last, First') 
    print('[3] Date: YYYY-MM-DD')
    print('[4] Archive')
    print('[5] Exit')

menu()
option = int(input('enter your search option: '))

while option != 5: 
    try: 
        field = option_table[option]
        search(field)
    except KeyError:
        print('Invalid choice. Choose between options 1 and 5')

    print()      
    menu()
    option = int(input('enter your search option: '))

print('Search Ended. Goodbye')


