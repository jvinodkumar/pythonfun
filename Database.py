
import sqlite3

db = sqlite3.connect("information.db")
db.row_factory = sqlite3.Row
attributes=dict()

def createTable():

    contactTableQuery = "create table if not exists contact(id integer primary key autoincrement, name text, email text, phone integer)"
    db.execute(contactTableQuery)
    db.commit()

def addData():

    name=input("\n\nEnter Name for the Contact Table : ")
    email = input("\nEnter Email for the Contact Table : ")
    phone = input("\nEnter Phone for the Contact Table : ")

    insertQuery = "insert into contact(name, email, phone) values('"+name+"','"+email+"',"+phone+");"
    print(insertQuery)
    db.execute(insertQuery)
    db.commit()
    print("Added 1 row successfully")

def updateData():

    contactID = input("\nEnter the contactID to be updated : ")
    newName = input("\nEnter new name : ")
    newEmail = input("\nEnter new email : ")
    newPhone = input("\nEnter new phone : ")
    updateQuery = "update contact set name='"+newName+"',email='"+newEmail+"',phone="+newPhone+" where id="+contactID+";"
    db.execute(updateQuery)
    db.commit()


def deleteData():
    contactID = input("\nEnter the contactID to be deleted : ")
    updateQuery = "delete contact where id="+contactID+";"
    db.execute(updateQuery)
    db.commit()

def closedb():
    db.close()

def main():

    createTable()


    print("\nSelect the operation you want to perform ")
    choice = input("\n1.Add Data \n3.Update Data \n4.Delete Data\n4.Exit")


    if choice=="1":
        addData()
    elif choice=="2":
        updateData()
    elif choice=="3":
        deleteData()
    else:
        closedb()
        print("Data management completed")





if __name__ == '__main__':main()


