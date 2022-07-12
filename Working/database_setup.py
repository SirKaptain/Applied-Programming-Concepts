from multiprocessing.sharedctypes import Value
from database_functions import *
import random
import string

# create a database connection
conn = create_connection('./Working/database.db') 

#creating necessary tables
create_table(conn, "LOGIN", "ID text primary key, PASSWORD text")
create_table(conn, "STUDENT", "ID int primary key, NAME text, SURNAME text, GRADYEAR int, MAJOR char(4), EMAIL text")
create_table(conn, "INSTRUCTOR", "ID int primary key, NAME text, SURNAME text, TITLE text, HIREYEAR int, DEPT char(4), EMAIL text")
create_table(conn, "ADMIN", "ID int primary key, NAME text, SURNAME text, TITLE text, OFFICE text, EMAIL text")
create_table(conn, "COURSES", "CRN int primary key, TITLE text, DEPT text, TIME text, DAYS_OF_WEEK text, SEMESTER text, YEAR int, CREDITS int")


login_attributes = []
for i in get_table_info(conn, "LOGIN"):
    login_attributes.append(i[1])

#populate login table
#generates 100 random id's and 6 character passwords
user_list = {}
for i in range(100):
    id = ("W00" + '{:06}'.format(random.randrange(1, 10**6)))
    password = ''.join(random.choice(string.ascii_uppercase + string.digits) for _ in range(4))
    insert_row(conn, "LOGIN", tuple(login_attributes), "('{}','{}')".format(id, password))
    


#ending for db modification
conn.commit()
conn.close()
