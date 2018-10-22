import ui

# A function to handle items on the menu.
def handle_choice(choice):

    if choice == '1':
        ui.create_product_table()
        ui.create_venue_table()
        ui.create_items_sold_table()
        print("Tables created successfully")

    elif choice == '2':

        '''Enter p for product table:
        Enter v for venue table:
        Enter i for items sold table'''
        table = input('Enter the table (p for product table; v for venue table; i for items sold table) ')
        if table == 'p':
           ui.add_new_product()
           print('Row entered successfully in product table')
        if table == 'v':
            ui.add_new_venue()
            print('Row entered successfully in venue table')
        if table == 'i':
            ui.add_new_item()
            print('Row entered successfully in sold items table')

    elif choice == '3':
        '''Enter p for product table:
        Enter v for venue table:
        Enter i for items sold table'''
        table = input('Enter the table (p for product table; v for venue table; i for items sold table) ')
        if table == 'p':
           ui.update_product_row()
           print('Row entered successfully in product table')
        if table == 'v':
            ui.update_venue_row()
            print('Row entered successfully in venue table')
        if table == 'i':
            ui.update_items_sold_row()
            print('Row entered successfully in sold items table')

    elif choice == '4':
        '''Enter p for product table:
        Enter v for venue table:
        Enter i for items sold table'''
        table = input('Enter the table (p for product table; v for venue table; i for items sold table) ')
        if table == 'p':

           ui.delete_product_row
           print('Row entered successfully in product table')
        if table == 'v':
            ui.delete_venue_row
            print('Row entered successfully in venue table')
        if table == 'i':
            ui.delete_items_sold_row
            print('Row entered successfully in sold items table')


    elif choice == '5':
        '''Enter p for product table:
        Enter v for venue table:
        Enter i for items sold table'''
        table = input('Enter the table (p for product table; v for venue table; i for items sold table) ')
        print('')
        if table == 'p':
            print('INVENTORY TABLE')
            print('---------------')
            ui.display_all_product_rows()

        if table == 'v':
            print('VENUE TABLE')
            print('-----------')
            ui.display_all_venue_rows()

        if table == 'i':
            print('SOLD ITEMS TABLE')
            print('-----------')
            ui.display_all_items_sold_rows()

    elif choice == '6':
        '''Enter p for product table:
        Enter v for venue table:
        Enter i for items sold table'''
        table = input('Enter the table (p for product table; v for venue table; i for items sold table) ')
        if table == 'p':

            ui.display_a_product_row()
            print('Row entered successfully in product table')
        if table == 'v':
            ui.display_a_venue_row()
            print('')
        # if table == 'i':
        #     ui.display_a_row()
        #     print('Row entered successfully in sold items table')

    elif choice == '7':
        ui.venue_sales_summary()
    elif choice == 'q' or choice == 'Q':
        print('Bye!')
        quit()

    else:
        ui.message('Please enter a valid selection\n')

# The program is run from the main function.
def main():
    quit = 'q'
    choice = None

    while choice != quit:
        choice = ui.display_menu_get_choice()
        handle_choice(choice)


if __name__ == '__main__':
    main()
