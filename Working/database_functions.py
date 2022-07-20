import sqlite3
from sqlite3 import Error

def create_connection(db_file):
    conn = None
    try:
        conn = sqlite3.connect(db_file)
    except Error as e:
        print(e)

    return conn

def create_table(conn, table, attribute):
    cur = conn.cursor()
    try:
        print("CREATE TABLE {} ({})".format(table, attribute))
        cur.execute("CREATE TABLE {} ({})".format(table, attribute))
    except Error as e:
        print(e)

def remove_table(conn, table):
    cur = conn.cursor()
    try:
        print("DROP TABLE {}".format(table))
        cur.execute("DROP TABLE {}".format(table))
    except Error as e:
        print(e)

def print_table(conn, table):
    cur = conn.cursor()
    try:
        print("SELECT * FROM {}".format(table))
        cur.execute("SELECT * FROM {}".format(table))
        print(cur.fetchall())
    except Error as e:
        print(e)

def search_table(conn, table, attribute, value):
    cur = conn.cursor()
    try:
        print("SELECT * FROM {} WHERE {} = '{}'".format(table, attribute, value))
        cur.execute("SELECT * FROM {} WHERE {} = '{}'".format(table, attribute, value))
        data = cur.fetchall()
        return data
    except Error as e:
        print(e)

def insert_row(conn, table, attributes, values):
    cur = conn.cursor()
    try:
        print("INSERT INTO {} {} VALUES {}".format(table, attributes, values))
        cur.execute("INSERT INTO {} {} VALUES {}".format(table, attributes, values))
    except Error as e:
        print(e)

def remove_row(conn, table, attribute, value):
    cur = conn.cursor()
    try:
        print("DELETE FROM {} WHERE {} = {}".format(table, attribute, value))
        cur.execute("DELETE FROM {} WHERE {} = {}".format(table, attribute, value))
    except Error as e:
        print(e)

def update_value(conn, table, id, id_value, attribute, new_value):
    cur = conn.cursor()
    try:
        print("UPDATE {} SET {} = '{}' WHERE {} = '{}'".format(table, attribute, new_value, id, id_value))
        cur.execute("UPDATE {} SET {} = '{}' WHERE {} = '{}'".format(table, attribute, new_value, id, id_value))
        data = cur.fetchall()
        return data
    except Error as e:
        print(e)

def get_table_names(conn):
    list = []
    cur = conn.cursor()
    try:
        print("SELECT name FROM sqlite_master WHERE type='table';")
        cur.execute("SELECT name FROM sqlite_master WHERE type='table';")
        tables = cur.fetchall()
        for i in tables:
            list.append(i[0])
        return list
    except Error as e:
        print(e)

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

def find_matching_instructors(conn):
    cur = conn.cursor()
    print("SELECT INSTRUCTOR.NAME, INSTRUCTOR.SURNAME, COURSES.TITLE FROM INSTRUCTOR INNER JOIN COURSES ON INSTRUCTOR.DEPT = COURSES.DEPT")
    cur.execute("SELECT INSTRUCTOR.NAME, INSTRUCTOR.SURNAME, COURSES.TITLE FROM INSTRUCTOR INNER JOIN COURSES ON INSTRUCTOR.DEPT = COURSES.DEPT")
    fetch = cur.fetchall()
    print(fetch)

def make_relation(conn, id_1, id_2):
    cur = conn.cursor()
    try:
        print("INSERT INTO SCHEDULE VALUES ({}, {})".format(id_1, id_2))
        cur.execute("INSERT INTO SCHEDULE VALUES ({}, {})".format(id_1, id_2))
    except Error as e:
        print(e)