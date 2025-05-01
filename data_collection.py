from data_collections.aybu_aybuzem_webscraper import aybuzem_scraper
from data_collections.aybu_schedule_scraper import schedule_scraper, sel_aybu_scraper
from data_collections.aybu_obs_html_scraper import obs_html_scraper
import time
import pandas as pd
import os
import sqlite3
from data_collections.constants import SQLITE_DATABASE

connection = sqlite3.connect(SQLITE_DATABASE)
c = connection.cursor()

c.execute(""" CREATE TABLE IF NOT EXISTS course_info(
          
          faculty_code text,
          faculty text,
          course_code text,
          course_name text,
          class text,
          teacher text,
          year integer,
          day text,
          start_time text,
          end_time text,
          student_nums integer,

          PRIMARY KEY(faculty_code)
        
)""")


"""

obs_html_files = os.listdir(os.path.join('data_collections', 'obs_html'))
print(obs_html_files)
print(len(obs_html_files))

# 1


    
with obs_html_scraper() as bot:

    counter = 0

    for html_file in obs_html_files:

        print(html_file)
        print('################################')

        bot.landing_page(html_file)
        bot.get_data()

        print('################################')

        counter = counter+1
        print(f'counter = {counter}')

    print(f'{counter} files have been done')



print('*****************************************')
"""

with aybuzem_scraper() as bot:

    # isletme faculty and its departements

    run = 0

    """

    while run < 4:

        bot.landing_page()
        bot.isletme_faculty()

        if run == 0:
        
            bot.ybs_departement()
            bot.scrape()

        elif run == 1:
            bot.fb_departement()
            bot.scrape()
        elif run == 2:

            bot.bus_departement()
            bot.scrape()
        elif run == 3:
            bot.itb_departement()
            bot.scrape()
        run = run+1
    """
    run = 0

    # insan faculty and its departements

    while run < 8:

        bot.landing_page()
        bot.insan_faculty()

        if run == 0:
            bot.TARİH_departement()
            bot.scrape()
        elif run == 1:
            pass
            #bot.PSİKOLOJİ_departement()
            #bot.scrape()
        elif run == 2:
            pass
            #bot.TÜRK_DİLİ_VE_EDEBİYATI_departement()
            #bot.scrape()
        elif run == 3:
            bot.FELSEFE_departement()
            bot.scrape()
        elif run == 4:
            pass
            #bot.SOSYOLOJİ_departement()
            #bot.scrape()
        elif run == 5:
            pass
            #bot.BİLGİ_VE_BELGE_YÖNETİMİ_departement()
            #bot.scrape()
        elif run == 6:
            pass
            #bot.DOĞU_DİLLERİ_VE_EDEBİYATLARI_departement()
            #bot.scrape()
        elif run == 7:
            pass
            #bot.MÜTERCİM_VE_TERCÜMANLIK_departement()
            #bot.scrape()

        run = run+1

    run = 0

    # ilahiyat faculty and its departements

    """

    while run < 1:

        bot.landing_page()
        bot.ilahiyat_faculty()

        if run == 0:
            bot.ilahiyat_departement()
            bot.scrape()
        
        run = run+1
    """
    run = 0

    # Mimarlık ve Güzel Sanatlar faculty and its departements
    """

    while run < 3:

        bot.landing_page()
        bot.Mimarlık_ve_Güzel_Sanatlar_faculty()

        if run == 0:
            bot.GÖRSEL_İLETİŞİM_TASARIMI_departement()
            bot.scrape()
        elif run == 1:
            bot.MİMARLIK_departement()
            bot.scrape()
        elif run == 2:
            bot.ENDÜSTRİYEL_TASARIM_departement()
            bot.scrape()
        
        run = run+1
    """

    run = 0

    # Sağlık Bilimleri faculty and its departements

    """

    while run < 8:

        bot.landing_page()
        bot.SAĞLIK_BİLİMLERİ_faculty()

        if run == 0:
            pass
            #bot.HEMŞİRELİK_departement()
            #bot.scrape()
        elif run == 1:
            bot.FİZYOTERAPİ_VE_REHABİLİTASYON_departement()
            bot.scrape()
        elif run == 2:
            bot.SOSYAL_HİZMET_departement()
            bot.scrape()
        elif run == 3:
            pass
            #bot.ODYOLOJİ_departement()
            #bot.scrape()
        elif run == 4:
            bot.ÇOCUK_GELİŞİMİ_departement()
            bot.scrape()
        elif run == 5:
            pass
            #bot.BESLENME_VE_DİYETETİK_departement()
            #bot.scrape()
        elif run == 6:
            pass
            #bot.SAĞLIK_YÖNETİMİ_departement()
            #bot.scrape()
        elif run == 7:
            pass
            #bot.DİL_VE_KONUŞMA_TERAPİSİ_departement()
            #bot.scrape()
        
        run = run+1

    """

    run = 0

    

    # Siyasal Bilgiler faculty and its departements

    """

    while run < 4:

        bot.landing_page()
        bot.SİYASAL_BİLGİLER_faculty()

        if run == 0:
            pass
            #bot.İKTİSAT_departement()
            #bot.scrape()
        elif run == 1:
            pass
            #bot.MALİYE_departement()
            #bot.scrape()
        elif run == 2:
            bot.SİYASET_BİLİMİ_VE_KAMU_YÖNETİMİ_departement()
            bot.scrape()
        elif run == 3:
            pass
            #bot.ULUSLARARASI_İLİŞKİLER_departement()
            #bot.scrape()
        run = run+1

    """

    run = 0

    


print('################################################')
#print_db_info()

"""
#2

def format_time(time_str):
    # Split the input by "." to correctly interpret hours and minutes
    hours, minutes = time_str.split(":")

    # Convert minutes to match the correct format (e.g., 5 → 50, 3 → 30)
    minutes = str(int(minutes) * 10) if len(minutes) == 1 else minutes

    # Ensure both hours and minutes are in two-digit format
    formatted_time = f"{int(hours):02}:{int(minutes):02}"

    return formatted_time


def merge_tables():



    logs = open('merge_logs.txt', 'a', encoding='utf-8')

    connection = sqlite3.connect(SQLITE_DATABASE)
    c = connection.cursor()

    c.execute('SELECT course_code FROM course_info')
    course_codes = c.fetchall()
    course_codes = list(set(course_codes))

    cc = []

    for code in course_codes:

        cc.append(code[0])

    course_codes = cc

    print(course_codes)
    logs.write(f'{course_codes}\n')

    c.execute('SELECT faculty FROM course_info')
    course_facultys = c.fetchall()
    course_facultys = list(set(course_facultys))

    ff = []

    for faculty in course_facultys:

        ff.append(faculty[0])

    course_facultys = ff
    print(course_facultys)
    logs.write(f'{course_facultys}\n')

    for code in course_codes:


        course_code = code

        # find the start time and the end time

        c.execute('SELECT start_time FROM course_info WHERE course_code = (?)', (course_code,))
        start_data = c.fetchall()

        c.execute('SELECT end_time FROM course_info WHERE course_code = (?)', (course_code,))
        end_data = c.fetchall()


        for i, data in enumerate(start_data):

            data = data[0].replace(":", ".")

            start_data[i] = float(data)

        print(f'new start_data is {start_data}')
        logs.write(f'new start_data is {start_data}\n')

        for i, data in enumerate(end_data):

            data = data[0].replace(":", ".")

            end_data[i] = float(data)

        print(f'new end_data is {end_data}')
        logs.write(f'new end_data is {end_data}\n')

        time_data = start_data+end_data
        print(f'time data is {time_data}')
        logs.write(f'time data is {time_data}\n')

        time_data = sorted(time_data)
        print(f'new time data is {time_data}')
        logs.write(f'new time data is {time_data}\n')



        class_start_time = format_time(str(time_data[0]).replace(".", ":"))
        class_end_time = format_time(str(time_data[-1]).replace(".", ":"))

        print(f'the class starts at {class_start_time} and ends at {class_end_time}')
        logs.write(f'the class starts at {class_start_time} and ends at {class_end_time}\n')

        # delete all the instances of a course except one

        print('################################################################')
        logs.write(f'################################################################\n')

        c.execute('SELECT * FROM course_info WHERE course_code = (?)', (course_code,))
        course_instances = c.fetchall()

        for course in course_instances:

            print(f'{course}\n\n')
            logs.write(f'{course}\n\n\n')

        for faculty in course_facultys:

            try:

                c.execute('''
                            DELETE FROM course_info 
                            WHERE ROWID NOT IN (
                                SELECT MIN(ROWID)
                                FROM course_info
                                WHERE course_code = ? AND faculty = ?
                                GROUP BY course_code, faculty
                            )
                            AND course_code = ? AND faculty = ?;
                        ''', (course_code, faculty, course_code, faculty))

                
                connection.commit()
                print(f'faculty deletion worked {faculty}')
                logs.write(f'faculty deletion worked {faculty}\n')

            except:

                print(f'faculty deletion did not work {faculty}')
                logs.write(f'faculty deletion did not work {faculty}\n')
        # update the remaining instance to have the latest end time

        try:

            c.execute("UPDATE course_info SET end_time = (?) WHERE course_code = (?)", (class_end_time, course_code,))
            connection.commit()
            print('update worked')
            logs.write(f'update worked\n')

        except:

            print('update did not work')
            logs.write(f'update did not work\n')

        # update the primary key

        print('#######################################')
        logs.write(f'#######################################\n')

        c.execute('SELECT faculty_code FROM course_info WHERE course_code = (?)', (course_code,))
        primary_key = c.fetchone()
        primary_key = primary_key[0]
        print(primary_key)
        logs.write(f'primary key = {primary_key}\n')

        point = primary_key.find('@')
        new_primary_key = primary_key[:point]
        print(new_primary_key)
        logs.write(f'new primary key = {new_primary_key}\n')

        try:

            c.execute('UPDATE course_info SET faculty_code = (?) WHERE faculty_code = (?)', (new_primary_key, primary_key,))
            connection.commit()
            print('primary key updated succesfully')
            logs.write(f'primary key updated succesfully\n')

        except:
            print('primary key update failed')
            logs.write(f'primary key update failed\n')

        # done now do a loop for all course codes
        # and maybe update the faculty_code, faculty to departement_code, departement
        # also make a backup db before running this function


merge_tables()

def print_db_info():
    connection = sqlite3.connect(SQLITE_DATABASE)
    c = connection.cursor()

    table_name = "course_info"  # Replace with your table name

    # Fetch and print all data
    c.execute(f"SELECT * FROM {table_name}")
    rows = c.fetchall()

    # Print column names
    columns = [desc[0] for desc in c.description]
    print("\t".join(columns))

    # Print each row
    for row in rows:
        print("\t".join(map(str, row)))

    # Close the connection
    connection.close()

print_db_info()
"""

#3
def db_to_csv():

    connection = sqlite3.connect(SQLITE_DATABASE)
    table_name = "course_info" 

    df = pd.read_sql_query(f'SELECT * FROM {table_name}', connection)

    print(df.head(5))
    df.to_html('sql_data.html', index=False, encoding='utf-8')
    df.to_csv('sql_data.csv', index=False, encoding='utf-8')


db_to_csv()





