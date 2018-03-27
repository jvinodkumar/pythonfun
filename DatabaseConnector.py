import sqlite3

db = sqlite3.connect("information.db")
db.row_factory = sqlite3.Row
attributes=dict()

def createTable():

    contactTableQuery = "create table if not exists contact(id integer primary key autoincrement, name text, email text, phone integer)"
    db.execute(contactTableQuery)
    db.commit()
