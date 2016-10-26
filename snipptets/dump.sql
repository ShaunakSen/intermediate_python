BEGIN TRANSACTION;
CREATE TABLE Employees(ID INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
     FName TEXT NOT NULL, LName TEXT NOT NULL, Age INTEGER NOT NULL,
     Address TEXT, Salary REAL, HireDate TEXT, 'Image' BLOB DEFAULT NULL);
INSERT INTO "Employees" VALUES(1,'Mini','Sen',20,'Bada Bazar Mohalla Jhansi',5000000.0,'2016-10-26',NULL);
DELETE FROM "sqlite_sequence";
INSERT INTO "sqlite_sequence" VALUES('Employees',2);
COMMIT;
