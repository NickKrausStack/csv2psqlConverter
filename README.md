# csv2psqlConverter 1.0
Converts a csv file to a postgres/psql database.

## REQUIREMENTS
If you have all these requirements, any or all of the 3 .py scripts should work right away:
You must have the psycopg2 package installed. (Easily done with PIP)
You must have postgres installed and running.
Obviously, you'll need at least one csv file as a source.
Create a blank postgres database in psql as your destination.
Remember to input your information (database name, password for postgres, etc.) in the beginning of the script you are using.

## ConvertCSVtoPostGres.py
This script uses 3 methods for the conversion process:
Create_table. Reads the header and first row of a csv file and uses that to create a sql create table command with column names and data type.
Insert data. Loops through the rows of the csv file and embeds them into sql-style insert commands.
Create_and_insert. both methods bundled into one for convenience.

There are 2 methods for the initial file reading process:
csv_folder. Loops through an entire folder, selects the csv files and calls the create and insert method to convert to Psql.
one_csv. Selects one csv file and passes it to the create and insert method to convert.

## SETPRIMARYKEY.py
Simple one-method script to assign primary keys to existing column in an existing table.
The source csv file should have these columns: tableName, constraintName, pkeyColumn. 
The exact column names for the csv don't matter, as long as you preserve the order of the columns.

## SETFOREIGNKEY.py
Another simple script, but for foreign keys.
The source csv file should have these columns: TableName, ConstraintName, FKey (name of column to use as foreign key), RefTable (table the foreignkey is referencing), RefColumn (matching column in that table).
The exact column names for the csv don't matter, as long as you preserve the order of the columns.
This will only work for an already-populated database that has declared primary keys/unique constraints for the existing tables.
