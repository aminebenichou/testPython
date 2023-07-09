import sqlite3


# function to initialize Database

def initialize(db_name):
    conn = sqlite3.connect(db_name)
    return conn

connection = initialize("todolist.db")
cursor = connection.cursor()


# function to create Table
# (Title text, Description text, status)
def createTable(table_name, table_columns):

    cursor.execute(f"""CREATE TABLE {table_name} {table_columns}""")


# Function to insert todo item

def insertValues(table_name, table_values):

    cursor.execute(f"""INSERT INTO {table_name} VALUES {table_values}""")


# function to fetch values

def fetchValues(table_name):

    cursor.execute(f"""SELECT * FROM {table_name}""")

print(cursor.fetchall())


