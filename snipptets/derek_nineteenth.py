# SQLite

import sqlite3
import sys


def printDB():
    try:
        result = theCursor.execute("SELECT ID, FName, LName, Age, Address, Salary, HireDate FROM Employees")
        for row in result:
            print("ID:", row[0])
            print("FName:", row[1])
            print("LName:", row[2])
            print("Age:", row[3])
            print("Address:", row[4])
            print("Salary:", row[5])
            print("HireDate:", row[6])

    except sqlite3.OperationalError:
        print("Table does not exists...")

    except:
        print("Error...")


# Create a SQLite db

db_conn = sqlite3.connect("test.db")

print("Database Created")

# Cursor is used to traverse the rrecords of the results

theCursor = db_conn.cursor()

# Instead of db_conn we can use theCursor to execute these commands as well

db_conn.execute('''
DROP TABLE IF EXISTS Employees
''')
db_conn.commit()

# Create a Table
try:
    db_conn.execute('''
    CREATE TABLE Employees(ID INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
     FName TEXT NOT NULL, LName TEXT NOT NULL, Age INTEGER NOT NULL,
     Address TEXT, Salary REAL, HireDate TEXT);
    ''')

    db_conn.commit()
except sqlite3.OperationalError:
    print("Table could not be created")

print("Table Created")

# INSERT

db_conn.execute('''
INSERT INTO Employees (FName, LName, Age, Address, Salary, HireDate) VALUES ('Mini', 'Sen', 20, 'Bada Bazar',
 5000000, date('now'))
''')

db_conn.execute('''
INSERT INTO Employees (FName, LName, Age, Address, Salary, HireDate) VALUES ('Shona', 'Sen', 23, 'Bada Bazar',
 5000000, date('now'))
''')

db_conn.commit()

printDB()

# UPDATE
try:
    db_conn.execute('''
    UPDATE Employees SET Address="Bada Bazar Mohalla Jhansi" WHERE ID=1
    ''')
    db_conn.commit()
except sqlite3.OperationalError:
    print("Table could not be updated")

printDB()

# DELETE
try:
    db_conn.execute('''
    DELETE FROM Employees WHERE ID=2
    ''')
    db_conn.commit()
except sqlite3.OperationalError:
    print("Table could not be deleted")

print("After Deletion...")
printDB()

# ROLL BACK THE LAST OPERATION

# db_conn.rollback()
# print("After Roll Back...")
# printDB()

# ADD NEW COLUMNS

try:
    db_conn.execute('''
    ALTER TABLE Employees ADD COLUMN 'Image' BLOB DEFAULT NULL
    ''')
    db_conn.commit()
except sqlite3.OperationalError:
    print("Table could not be altered")

theCursor.execute("PRAGMA TABLE_INFO(Employees)")
# print(theCursor.fetchall())
rowNames = [nameTuple[1] for nameTuple in theCursor.fetchall()]
print(rowNames)
# Total Rows in db

theCursor.execute("SELECT COUNT(*) FROM Employees")

numOfRows = theCursor.fetchall()
print("Total Rows: ", numOfRows[0][0])

# GET SQLite version we are working with


theCursor.execute("SELECT SQLITE_VERSION()")
print("SQLite Version:", theCursor.fetchone())

# DICTIONARY CURSOR to retrieve data in a dictionary

with db_conn:
    db_conn.row_factory = sqlite3.Row

    theCursor = db_conn.cursor()
    theCursor.execute("SELECT * FROM Employees")
    rows = theCursor.fetchall()

    for row in rows:
        print("{} {}".format(row['FName'], row['LName']))

# Write Data to a file

# Useful for backing up a database


with open('dump.sql', 'w') as f:
    for line in db_conn.iterdump():
        f.write("%s\n" % line)

db_conn.close()

print("Database Closed")
