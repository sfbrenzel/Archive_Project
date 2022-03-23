import pandas as pd  
import plotly.express as px

from tabulate import tabulate


#import data for data search 
tdb = pd.read_csv('Tables/NTTable.csv')


#search dictionary: for possible names, see NTTable.csv
s_option_table = {1: 'Sender', 2: 'Recipient', 3: 'Date', 4: 'Archive'}

#search function
def search(s_field):
    search_q = input(f'Please enter {s_field}: ')
    search_a = tdb.loc[tdb[s_field] == search_q]
    if len(search_a) > 0: 
        print(tabulate(search_a, headers='keys', tablefmt='fancy_grid'))
    else: 
        print(f'{s_field} not found in database')


#visual dictionary: for possible names, see NTTable.csv
v_option_table = {1: 'Sender', 2: 'Recipient'}

#visual function 
def visual(v_field): 
    top_ten_s = tdb['Sender'].value_counts().head(10)
    top_ten_r = tdb['Recipient'].value_counts().head(10)
    visual_q = input(f'Please enter {v_field}: ')
    visual_s = px.pie(top_ten_s, values = '# of Letters', names = 'Senders', title = 'Archive Breakdown')
    visual_r = px.pie(top_ten_r, values = '# of Letters', names = 'Recipients', title = 'Archive Breakdown')
    if len(visual_q) > 0:
        print(visual_s)
    elif len(visual_q) > 0: 
        print(visual_r)
    else: 
        print(f'{v_field} not found in database')


#search menu
def s_menu(): 
    print('[1] Sender: Last, First')
    print('[2] Recipient: Last, First') 
    print('[3] Date: YYYY-MM-DD')
    print('[4] Archive')
    print('[5] Exit')

s_menu()
s_option = int(input('enter your search option: '))

while s_option != 5: 
    try: 
        s_field = s_option_table[s_option]
        search(s_field)
    except KeyError:
        print('Invalid choice. Choose between options 1 and 5')

    print()      
    s_menu()
    s_option = int(input('enter your search option: '))

print('Program Ended. Goodbye')


#visual menu 
def v_menu(): 
    print('[1] Sender: Last, First')
    print('[2] Recipient Last, First')
    print('[3] Exit')

v_menu()
v_option = int(input('enter your visualization option: '))

while v_option != 3: 
    try: 
        v_field = v_option_table[v_option]
        visual(v_field)
    except KeyError: 
        print('Invalid choice. Choose between options 1 and 3')

    print()
    v_menu()
    v_option = int(input('enter your visualization option: '))

print('Program Ended. Goodbye')


#main menu 
def m_menu(): 
    print('[1] Search Database')
    print('[2] Visualize Database')
    print('[3] Exit')

m_menu() 
m_option = int(input('Choose search or visualize: '))

while m_option != 3: 
    if m_option == 1: 
        s_menu()
    elif m_option == 2:
        v_menu()
    else: 
        print('Invalid choice. Choose options 1 or 2')

    print()
    m_menu() 
    m_option = int(input('Choose search or visualize'))

print('Program Ended. Goodbye')

#main function 
def main(): 
  first_m = m_menu()
  second_m = s_menu()
  third_m = v_menu() 


if __name__ == '__main__':
    main()


