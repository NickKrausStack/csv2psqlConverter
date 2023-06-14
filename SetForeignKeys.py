import csv
import os

#This allows the user to write up the foreign key columns  for an entire postgres database in a csv file and then upload to postgres with a single run.
#the database, tables, and columns must already exist. Primary keys or unique constraints must already be declared.
#The csv file should be formatted with columns in this order: Table, constraintName, ForeignKeyColumn, RefTable (table your ForeignKey refers to), RefColumn.
# (exact column names don't matter)

#modify these parameters:
host = 'localhost'
database = 'yourdatabasename'
user = 'postgres'
password = 'SomePassword'
#path to your csv foreign key file:
pathh = "C:\\Users\\nechk\\OneDrive\\Desktop\\schooldatakeys\\foreignkey.csv"

def set_fkeys(pkeyfile, dbname):
    conn = psycopg2.connect(host=host, database=database, user=user, password=password)
    cursor = conn.cursor()
 
    with open(pkeyfile, 'r') as file:
        csv_data = csv.reader(file)
        headers = next(csv_data)
        for row in csv_data:   
            addkey = "ALTER TABLE %s ADD CONSTRAINT %s FOREIGN KEY (%s) REFERENCES %s(%s);" % (*row,)
            print(addkey)
            cursor.execute(addkey)
            print("added.")
        conn.commit()
        cursor.close()
        conn.close()

#run method
set_fkeys(pathh, db)
