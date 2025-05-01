from data_collections.aybu_obs_csv_scraper import csv_scraper
from data_collections.constants import SQLITE_DATABASE
csv_file ='sağlık bilimleri fakültesi.html'
csv_file2 = 'isletme.html'
csv_file3 = 'islami ilimler.html'
csv_file4 = 'insan ve toplum bilimleri.html'
import sqlite3
import pandas as pd
import os

"""
connection = sqlite3.connect(SQLITE_DATABASE)
c = connection.cursor()

c.execute('SELECT * FROM course_info')
sql_data = c.fetchall()

csv_data = pd.read_sql('SELECT * FROM course_info', connection)
csv_data.to_csv('csv_data_.csv')

for row in sql_data:
    print(f'{row}\n')
"""

with csv_scraper() as bot:

    bot.isletme_landing_page(os.path.join('obs_html',csv_file2))
    bot.isletme_get_data()
    bot.landing_page(os.path.join('obs_html',csv_file))
    bot.get_data()
    bot.landing_page(os.path.join('obs_html',csv_file3))
    bot.get_data()
    bot.landing_page(os.path.join('obs_html',csv_file4))
    bot.get_data()

def db_to_csv():

    connection = sqlite3.connect(SQLITE_DATABASE)
    table_name = "course_info" 

    df = pd.read_sql_query(f'SELECT * FROM {table_name}', connection)

    print(df.head(5))
    df.to_html('sql_data.html', index=False, encoding='utf-8')
    df.to_csv('sql_data.csv', index=False, encoding='utf-8')


db_to_csv()


