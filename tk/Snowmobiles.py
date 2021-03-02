import sqlite3
from tkinter import *

def create_table():
    #connect to db
    conn = sqlite3.connect("lite.db")

    #create cursor object
    cur = conn.cursor()

    #write an SQL query
    cur.execute("CREATE TABLE IF NOT EXISTS store (item TEXT, quantity INTEGER , price REAL )")

    #commit changes
    conn.commit()

    #close connection to db
    conn.close()

def insert(item, quantity, price):
    #connect to db
    conn = sqlite3.connect("lite.db")

    #create cursor object
    cur = conn.cursor()

    #write an SQL query
    cur.execute("INSERT INTO store VALUES (?,?,?)", (item,quantity,price))

    #commit changes
    conn.commit()

    #close connection to db
    conn.close()

def view():
    # connect to db
    conn = sqlite3.connect("lite.db")

    # create cursor object
    cur = conn.cursor()

    # write an SQL query
    cur.execute("SELECT * FROM store")

    #fetch data
    rows = cur.fetchall()

    # close connection to db
    conn.close()

    #return what was fetched
    return rows

def delete(item):
    # connect to db
    conn = sqlite3.connect("lite.db")

    # create cursor object
    cur = conn.cursor()

    # write an SQL query
    cur.execute("DELETE FROM store WHERE item=?", (item,))

    # commit changes
    conn.commit()

    # close connection to db
    conn.close()

    #return what was fetched
    return rows

def update(quantity,price,item):
    # connect to db
    conn = sqlite3.connect("lite.db")

    # create cursor object
    cur = conn.cursor()

    # write an SQL query
    cur.execute("UPDATE store SET quantity=?, price=? WHERE item=?",(quantity,price,item))

    # commit changes
    conn.commit()

    # close connection to db
    conn.close()

update(11,6,"Water Glass")
print(view())