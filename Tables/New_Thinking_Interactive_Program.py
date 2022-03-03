import pandas as pd 

#import data 
tdb = pd.read_csv('Tables/NTTable.csv')

#define terms 
def sender_search():
    sender_q = input("Please enter sender's last name, first name ")
    try: 
        print(tdb.loc[tdb['Sender'] == sender_q])
    except: 
        print('Sender is not in the database.')


def recipient_search():
    recipient_q = input("Please enter recipient's last name, first name ")
    try: 
       print(tdb.loc[tdb['Recipient'] == recipient_q])
    except: 
        print('Recipient is not in the database')


def date_search(): 
    date_q = input("please enter date YYYY-MM-DD ")
    try: 
        print(tdb.loc[tdb['Date'] == date_q])
    except: 
        print('Date not found')

def archive_search():
    archive_q = input("please enter archive location ")
    try: 
        print(tdb.loc[tdb.Archive == archive_q])
    except: 
        print('Letter not found in this archive.')

#main menu
def menu(): 
    print('[1] Sender')
    print('[2] Recipient') 
    print('[3] Date')
    print('[4] Archive')
    print('[5] Exit')

menu()
option = int(input('enter your search option: '))

while option != 5: 
    if option == 1:
        sender_search()
    elif option == 2:
        recipient_search()
    elif option == 3:
        date_search()
    elif option == 4: 
        archive_search()
    else: 
        print('Invalid Search Option') 

    print()      
    menu()
    option = int(input('enter your search option: '))

print('Search Ended. Goodbye')

#store user input 
#display table 
