import sqlite3

import pandas as pd

db = 'product_db.db'

def display_menu_get_choice():
    print('MAKE SELECTION FROM THE MENU')
    '''Display choices for user, return users' selection'''
    print('''

        1. create a database and a table
        2. Add a row of data to the database table
        3. update a row in the database table
        4. Delete a row from the database table
        5. Display all the rows in the database table
        6. Display a single row of data based on an input
        7. Display venue_sales_summary
        q. Quit

    ''')

    choice = input('Enter your selection: ')

    return choice

# Connect to the database.
conn = sqlite3.connect(db)
cur = conn.cursor()
print ("Opened database successfully\n")

# Create a table PRODUCT in the database.
def create_product_table():
    conn.execute('''CREATE TABLE IF NOT EXISTS PRODUCT
        (ID                     INT    PRIMARY KEY     NOT NULL,
        NAME                    TEXT    NOT NULL,
        DESCRIPTION             TEXT     NOT NULL,
        UNIT_PRICE              REAL,
        IN_STOCK                INT)''')

    return
# conn.execute('drop table PRODUCT')
# Create a table VENUE in the database.
def create_venue_table():
    conn.execute('''CREATE TABLE IF NOT EXISTS VENUE
        (VENUE_ID               INT    PRIMARY KEY     NOT NULL,
        NAME                    TEXT    NOT NULL,
        LOCATION                TEXT     NOT NULL,
        EVENT_DATE              DATE )''')
    return

def create_items_sold_table():
    conn.execute('''CREATE TABLE IF NOT EXISTS ITEMS_SOLD
        (ID                     INT    PRIMARY KEY     NOT NULL,
        NAME                    TEXT    NOT NULL,
        DESCRIPTION             TEXT     NOT NULL,
        UNIT_PRICE              REAL,
        QTY                     INT,
        VENUE_ID                INT,
        FOREIGN KEY (VENUE_ID) REFERENCES VENUE(VENUE_ID))''')
conn.commit()
# conn.execute('drop table VENUE')
# Add new product rows to the table.
def add_new_product():

    ID = input('Enter product id: ')
    NAME = input('Enter name of product: ')
    DESCRIPTION = input('Enter product description: ')
    UNIT_PRICE = input('Enter product unit price: ')
    IN_STOCK = input('Enter the quantity on hand (enter an integer): ')
    print(' ')
    create_product_table()
    conn.execute('INSERT INTO PRODUCT VALUES (?,?,?,?,?)', (ID, NAME, DESCRIPTION, UNIT_PRICE, IN_STOCK))
    conn.commit()
    print('')
    return

# Add new new rows to the venue table.
def add_new_venue():
    VENUE_ID = input('Enter a venue ID:  ')
    NAME = input('Enter the name of the event: ')
    LOCATION = input('Enter the location: ')
    EVENT_DATE = input('Enter the date: ')
    print('')
    create_venue_table()
    conn.execute('INSERT INTO VENUE VALUES (?,?,?,?)', (VENUE_ID, NAME, LOCATION, EVENT_DATE))
    conn.commit()
    print('')
    return

# Add new item rows to the items_sold table.
def add_new_item():
    ID = input('Enter product id: ')
    NAME = input('Enter name of product: ')
    DESCRIPTION = input('Enter product description: ')
    UNIT_PRICE = input('Enter product unit price: ')
    QTY = input('Enter quantity of item sold: ')
    VENUE_ID = input('Enter the venue id ')
    print(' ')
    create_product_table()
    create_items_sold_table()
    conn.execute('INSERT INTO ITEMS_SOLD VALUES (?,?,?,?,?,?)', (ID, NAME, DESCRIPTION, UNIT_PRICE, QTY, VENUE_ID))
    cur.execute("UPDATE PRODUCT SET IN_STOCK = IN_STOCK - ?  WHERE ID = ?",(QTY, ID) )
    conn.commit()
    print('')
    return

# Show all the product rows in the table.
def display_all_product_rows():
    df = pd.read_sql_query("SELECT * FROM PRODUCT", conn)
    print(df)
    print('')
    return

# Show all the rows in the venue table.
def display_all_venue_rows():
    df = pd.read_sql_query("SELECT * FROM VENUE", conn)
    print(df)
    print('')
    return

def display_all_items_sold_rows():
    df = pd.read_sql_query("SELECT * FROM ITEMS_SOLD", conn)
    print(df)
    print('')
    return
# Update a row in the product table and save the changes.
def update_product_row():
    id = input('Enter ID: ')
    qty = input('Enter quantity to be added to product table: ')
    create_product_table()
    c = cur.execute("UPDATE PRODUCT SET IN_STOCK = IN_STOCK + ?  WHERE ID = ?",(qty, id) )
    conn.commit()
    return

# update a row in the venue table
def update_venue_row():
    id = input('Enter ID: ')
    price = input('Enter the new price: ')
    create_venue_table()
    c = cur.execute("UPDATE VENUE SET UNIT_PRICE = ?  WHERE ID = ?",(price, id) )
    conn.commit()
    return

def update_items_sold_row():
    id = input('Enter ID: ')
    price = input('Enter the new price: ')
    create_items_sold_table()
    c = cur.execute("UPDATE ITEMS_SOLD SET UNIT_PRICE = ?  WHERE ID = ?",(price, id) )
    conn.commit()
    return
# Delete a row in the table and save the changes
def delete_product_row():
    id = input('Enter ID ')
    c = cur.execute("DELETE FROM PRODUCT WHERE ID = ?", (id,))
    conn.commit()

def delete_venue_row():
    id = input('Enter ID ')
    c = cur.execute("DELETE FROM VENUE WHERE ID = ?", (id,))
    conn.commit()

def delete_items_sold_row():
    id = input('Enter ID ')
    c = cur.execute("DELETE FROM ITEMS_SOLD WHERE ID = ?", (id,))
    conn.commit()
# Display a single row in the table.
def display_a_product_row():
    id  = input('Enter the ID: ',)
    print('')
    c = cur.execute("SELECT * FROM  PRODUCT WHERE ID = ?", \
    (id,)).fetchall()
    if len(c) == 0:
        print ('* No items *')
    else:
        # print(c.fetchall())
        # print(c)
        for row in c:
            print("ID = ", row[0])
            print("NAME = ", row[1])
            print("LOCATION = ", row[2])
            print("UNIT_PRICE = ", row[3])
            print("IN_STOCK = ", row[4], "\n")


def display_a_venue_row():
    id  = input('Enter the ID: ',)
    print('')
    c = cur.execute("SELECT * FROM VENUE  WHERE VENUE_ID = ?", \
    (id,)).fetchall()
    if len(c) == 0:
        print ('* No items *')
    else:
        # print(c.fetchall())
        # print(c)
        for row in c:
            print("VENUE_ID = ", row[0])
            print("NAME = ", row[1])
            print("DESCRIPTION = ", row[2])
            print("EVENT_DATE = ", row[3],"\n")

def venue_sales_summary():
    s = 0

    id  = input('Enter the ID: ',)
    print('')
    c = cur.execute("SELECT VENUE.NAME, VENUE.LOCATION, ITEMS_SOLD.NAME, ITEMS_SOLD.UNIT_PRICE,\
    ITEMS_SOLD.QTY, ITEMS_SOLD.UNIT_PRICE*ITEMS_SOLD.QTY as sub_total \
    FROM VENUE JOIN ITEMS_SOLD ON VENUE.VENUE_ID = ITEMS_SOLD.VENUE_ID\
    WHERE VENUE.VENUE_ID = ?", (id,)).fetchall()
    df = pd.DataFrame(c, columns = list('ELIPQT'))
    print(df)

    row_count = len(c)
    i = 0
    while i < row_count:
    #     # print('')
        s = s+c[i][5]
        i=i+1
    print('')

    print('Total sales = $',s,"\n")

    print('E = event name')
    print('L = location')
    print('I = items sold')
    print('P = unit price')
    print('Q = quantity')
    print('T = sub_total\n')

def message(msg):
    '''Display a message to the user'''
    print(msg)
