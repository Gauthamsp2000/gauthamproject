import pathlib
import sqlite3
import pandas as pd
from pathlib import Path


path = Path().cwd()#None # use pathlib to get current working directory


def create_db(db_name, filename, table_name):
 
    con = sqlite3.connect(db_name)#None # create a connection to the database
    cursor = con.cursor()#None # create a cursor

    Electronic= pd.read_csv(filename) #None # read in the data 
    # insert the data into the specified table 
    Electronic.to_sql(table_name,con,if_exists='replace',index=False)
    # execute a select statement as f-string and print results to verify insertion
    cursor.execute(f"SELECT * FROM {table_name}").fetchall()
    # commit the changes to the database
    con.commit()
    # close the connection
    con.close()

if __name__=="__main__":
    db_name = "Electronic.db"
    filename = "Electronic.csv"
    table_name = "electronic"
    create_db(db_name, filename, table_name)
