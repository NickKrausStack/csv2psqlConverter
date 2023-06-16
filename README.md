# csv2psqlConverter 1.0
Converts a csv file or group of files to a postgres/psql database.

## REQUIREMENTS
If you have all of the following requirements, any or all of the 3 .py scripts should work right away.
The psycopg2 package must be installed. (Easily done with PIP)
Postgres must be installed and running.
Obviously, you'll need at least one csv file as a source and a blank postgres database as a destination.
Input the relevant information (database name, password for postgres, etc.) in the beginning of the script you are using.

## ConvertCSVtoPostGres.py
This script uses 3 methods for the conversion process: 1) Create_table reads the header and first row of a csv file and uses that to create a create table command with column names and data type. 2) Insert data loops through the rows of the csv file and embeds them into sql-style insert commands to populate the Postgres database. 3) Create_and_insert combines both methods for convenience.

There are 2 methods for the initial file reading process: 1) csv_folder loops through an entire folder, selects the csv files and calls the create and insert methods to convert.
2) One_csv selects just one csv file and passes it to the create and insert methods to convert.

## SETPRIMARYKEY.py
This is a simple one-method script to assign primary keys to existing column in an existing table. This is particularly useful if you have a bunch of tables in a Postgres database and need to map out the primary and foreign keys. With this script, you can just type it all out in a csv file and then port it to your database with one run.
The source csv file should have these columns populated with the appropriate data: tableName, constraintName, pkeyColumn. 
The exact column names for the csv don't matter, as long as you preserve the order of the columns.

## SETFOREIGNKEY.py
Same as above, but for foreign keys. The source csv file should have these columns: TableName, ConstraintName, FKey (name of column to use as foreign key), RefTable (table the foreignkey is referencing), RefColumn (matching column in that table). Again, the exact column names for the csv don't matter, as long as you preserve the order of the columns.
NOTE: This will only work for an already populated database that has declared primary keys/unique constraints for the existing tables. All ordinary rules of primary/foreign keys must be adhered to in order for it to succeed.
