#simple script to  assign primary keys to a local Postgres database tables using a source csv file.
#the csv file should have the following columns: table, constraintName, PrimaryKeyColumn.

#add primary keys from tables
import psycopg2
import csv
import os

pathh = "C:\\path to csv file"
db = 'dbname'
host = 'localhost'
database = db
user = 'postgres'
password = 'SomePassword'

def set_pkeys(pkeyfile, db):
    conn = psycopg2.connect(host=host, database=database, user=user, password=password)
    cursor = conn.cursor()
 
    with open(pkeyfile, 'r') as file:
        csv_data = csv.reader(file)
        headers = next(csv_data)
        for row in csv_data:   
            addkey = "ALTER TABLE %s ADD CONSTRAINT %s ADD PRIMARY KEY (%s);" % (*row,)
            print(addkey)
            cursor.execute(addkey)
            print("added.")
        conn.commit()
        cursor.close()
        conn.close()

set_pkeys(pathh, db)
