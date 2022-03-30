import pandas as pd  
import matplotlib.pyplot as plt
from tabulate import tabulate


#import data for data search 
tdb = pd.read_csv('Tables/NTTable.csv')


#search dictionary: for possible names/dates/archives to search, see NTTable.csv or pie chart 
s_option_table = {1: 'Sender', 2: 'Recipient', 3: 'Date', 4: 'Archive'}

#search function
def search(s_field):
    search_q = input(f'Please enter {s_field}: ')
    search_a = tdb.loc[tdb[s_field] == search_q]
    if len(search_a) > 0: 
        print(tabulate(search_a, headers='keys', tablefmt='fancy_grid'))
    else: 
        print(f'{s_field} not found in database') 


#visual function 
def visual(): 
    top_ten_s = tdb.groupby(['Sender'])['Sender'].count().sort_values(ascending=False).head(10)
    top_ten_s.plot.pie(title='Breakdown of Database', figsize=[8,8], autopct='%.2f')
    plt.show()


#search menu
def s_menu(): 
    print('[1] Sender: Last, First')
    print('[2] Recipient: Last, First') 
    print('[3] Date: YYYY-MM-DD')
    print('[4] Archive')
    print('[5] Exit')


    s_option = int(input('Enter selection: '))
    if s_option.isdigit() != True: 
        raise ValueError('Invalid Entry. Choose between 1 and 5')


    while True: 
        if s_option == 5:
            m_menu()
            break
        else: 
            try: 
                s_field = s_option_table[s_option]
                search(s_field)
            except KeyError:
                print('Invalid entry. Choose between 1 and 5')
            

        print()      
        s_menu()
    

#main menu 
def m_menu(): 
    print('[1] Search Database')
    print('[2] Visualize Database')
    print('[3] Exit')

   
    m_option = int(input('Enter selection: '))


    while True: 
        if m_option == 1: 
            s_menu()
            break
        elif m_option == 2:
            visual()
            m_menu()
            break
        elif m_option == 3: 
            print('Program ended. Goodbye')
            exit()
        else: 
            print('Invalid entry. Choose options 1 or 2')


        print()
        m_menu() 
    

#main function 
def main(): 
  m_menu()
  print('Program Ended. Goodbye')
  


if __name__ == '__main__':
    main()


