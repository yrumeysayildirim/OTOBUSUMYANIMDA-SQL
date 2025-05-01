import time
import pandas as pd
import os
import sqlite3
from data_collections.constants import SQLITE_DATABASE, SQLITE_DATABASE_MODEL



def db_to_csv():

    connection = sqlite3.connect(SQLITE_DATABASE_MODEL)
    table_name = "course_info" 

    df = pd.read_sql_query(f'SELECT * FROM {table_name}', connection)

    print(df.head(5))
    df.to_html('sql_data_m.html', index=False, encoding='utf-8')
    df.to_csv('sql_data_m.csv', index=False, encoding='utf-8')


db_to_csv()




