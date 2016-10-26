# SQLite

import sqlite3
import sys

# Create a SQLite db

db_conn = sqlite3.connect("test.db")

print("Database Created")

# Cursor is used to traverse the rrecords of the results

theCursor = db_conn.cursor()

# Create a Table

theCursor.execute('''
CREATE TABLE IF NOT EXISTS Employees(ID INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
 FName TEXT NOT NULL, LName TEXT NOT NULL, Age INTEGER NOT NULL,
 Address TEXT, Salary REAL, HireDate TEXT);
''')

db_conn.commit()

print("Table Created")




db_conn.close()

print("Database Closed")