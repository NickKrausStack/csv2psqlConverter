import psycopg2
import csv
import os

#insert the relevant data for these parameters

host = 'localhost'
user = 'postgres'
password = 'SomePassword'
folderpath = "C:\\path to csv folder" #use if you want to convert an entire folder 
singleCsv = "C:\\path to csv file" #use if you want to convert just one file
dbname = Name of destination psql database 

#By default, the last lines of code will run the convert folder and convert file methods, scroll to the end and remove or comment whichever you don't want.

#converts each csv file in the parameter separately into its own Postgres table, assigning columns and column types (integer or varchar)
#assumes the csv starts with an ID column meant to be the primary key.

def createtables(newpath,filename, dbname):
    conn = psycopg2.connect(host=host, database=database, user=user, password=password)
    cursor = conn.cursor()
 
    with open(newpath, 'r',encoding='utf-8-sig', errors='replace') as file:
        csv_data = csv.reader(file)
        headers = next(csv_data)
        secondrow = next(csv_data)

        column_data_types = [] 
        for col in headers:
            if col =="ID":
               cdata_type = 'INTEGER' 
            else:
                if secondrow[headers.index(col)].isdigit():
                    cdata_type = 'INTEGER CHECK ('+col+ " IS NULL OR "+col+" >= 0)" #need IS NULL to handle blank cells.
                else:  
                    cdata_type = 'VARCHAR(255)'
            column_data_types.append(cdata_type)

        column_definitions = [f"{col} {data_type}" for col, data_type in zip(headers, column_data_types)] 
        create_table_sql = f"CREATE TABLE IF NOT EXISTS {filename} ({', '.join(column_definitions)})"
        print("CREATE TABLE SQL:", create_table_sql)
        cursor.execute(create_table_sql)
        print("tables created")

        conn.commit()
        cursor.close()
        conn.close()

#insert data method -- follows the previous method in populating the created postgres table with all the data from the csv.

def insertdata(newpath,filename, dbname):
    conn = psycopg2.connect(host=host, database=dbname, user=user, password=password)
    cursor = conn.cursor()

    with open(newpath, 'r',encoding='utf-8-sig', errors='replace') as file:
        csv_data = csv.reader(file)
        headers = next(csv_data)
        insert_sql = f"INSERT INTO {filename} ({','.join(headers)}) VALUES ({','.join(['%s'] * len(headers))})"
        print("INSERT SQL:", insert_sql)

        for row in csv_data:
                row = [value if value != '' else None for value in row] #again, we need the None to handle any blank cells. 
                try:
                    cursor.execute(insert_sql, row)
                except UnicodeDecodeError:
                    print("Decoding error in row:", row)
        print("data inserted.")
        conn.commit()
        cursor.close()
        conn.close()

#this method just puts the previous two together for convenience.
def create_and_insert(newpath,filename, dbname):
    createtables(newpath,filename, dbname),
    insertdata(newpath,filename, dbname)

#this method will loop through any folder, locating .csv files and running the create_and_insert method. It 
def csv_folder(source_folder, dbname):
    for filename in os.listdir(source_folder):
        if filename.lower().endswith(".csv"):
            JustName = os.path.splitext(filename)[0]
            print(JustName)
            newpath = source_folder+"\\"+filename 
            create_and_insert(newpath,JustName0, dbname)

def one_csv(source_file, dbname):
            filename = os.path.basename(source_file)
            filename = os.path.splitext(filename)[0]
            print(filename)
            create_and_insert(source_file,filename, dbname)

#run the methods:
whole_folder(folderpath, dbname)
one_csv(singleCsv,dbname)
