import sqlite3 as sq


def connectDB(name):
    connection = sq.connect(name)
    return connection


def getCursor(connection):
    cursor = connection.cursor()
    return cursor


def create_table_Description(cursor):
    cursor.execute('''
    create table Description (
        id int primary key, 
        Description text
    )
    ''')


def create_table_Book(cursor):
    cursor.execute('''
    create table Book (
        id int primary key, 
        Title text,
        Category text,
        Price float,
        Price_After_Tax float,
        Tax_amount float,
        Avilability float,
        Number_of_reviews float,
        Stars float,
        Book_Description int,
        foreign key(Book_Description) references Description(id)
    )
    ''')
