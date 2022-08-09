import sqlite3
from sqlite3 import Error


#Input: directory of database file
#Return: connection object
def create_connection(db_file):
    conn = None
    try:
        conn = sqlite3.connect(db_file)
    except Error as e:
        print(e)

    return conn

#Input: connection object, table name as a string, attributes as a comma delimited string
#Return: N/A
def create_table(conn, table, attribute):
    cur = conn.cursor()
    try:
        cur.execute("CREATE TABLE {} ({})".format(table, attribute))
    except Error as e:
        print(e)

#Input: connection object, table name as a string
#Return: N/A
def remove_table(conn, table):
    cur = conn.cursor()
    try:
        cur.execute("DROP TABLE {}".format(table))
    except Error as e:
        print(e)

#Input: connection object, table name as a string
#Return: List of rows as a tuple
def get_table(conn, table):
    cur = conn.cursor()
    try:
        cur.execute("SELECT * FROM {}".format(table))
        return cur.fetchall()
    except Error as e:
        print(e)

#Input: connection object, table name as a string, attribute as a string, value as a string
#Return: list of searched row as tuple
def search_table(conn, table, attribute, value):
    cur = conn.cursor()
    try:
        cur.execute("SELECT * FROM {} WHERE {} = '{}'".format(table, attribute, value))
        data = cur.fetchall()
        return data
    except Error as e:
        print(e)

#Input: connection object, table name as a string, attributes as a comma delimited string, values as a tuple
#Return: N/A
def insert_row(conn, table, attributes, values):
    cur = conn.cursor()
    try:
        cur.execute("INSERT INTO {} {} VALUES {}".format(table, attributes, values))
    except Error as e:
        print(e)

#Input: connection object, table name as a string, attribute as a string, value as a string
#Return: N/A
def remove_row(conn, table, attribute, value):
    cur = conn.cursor()
    try:
        cur.execute("DELETE FROM '{}' WHERE '{}' = '{}'".format(table, attribute, value))
    except Error as e:
        print(e)

#Input: connection object, table name as a string, attribute as string, new_value as string, primary key as string, old_value as string 
#Return: N/A
def update_value(conn, table, attribute, new_value, primary_key, old_value):
    cur = conn.cursor()
    try:
        cur.execute("UPDATE {} SET {} = '{}' WHERE {} = '{}'".format(table, attribute, new_value, primary_key, old_value))
    except Error as e:
        print(e)

#Input: connection object
#Return: List of tables as strings
def get_table_names(conn):
    list = []
    cur = conn.cursor()
    try:
        cur.execute("SELECT name FROM sqlite_master WHERE type='table' ORDER BY name ASC;")
        tables = cur.fetchall()
        for i in tables:
            list.append(i[0])
        return list
    except Error as e:
        print(e)

#Input: connection object, table name as string
#Return: List of table info as tuples
def get_table_info(conn, table):
    list = []
    cur = conn.cursor()
    try:
        cur.execute("PRAGMA table_info({})".format(table))
        info = cur.fetchall()
        for i in info:
            list.append(i)
        return list
    except Error as e:
        print(e)

#Input: connection object, table name as string
#Return: List of table attributes as strings
def get_attributes(conn, table):
    attributes = []
    for i in get_table_info(conn, table):
        attributes.append(i[1])
    return attributes
