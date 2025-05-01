from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from data_collections.constants import SQLITE_DATABASE
import os
import pandas as pd
import sqlite3
import time
import re

main_path = os.path.join('data_collections','obs_html')

class obs_html_scraper(webdriver.Chrome):

    def __init__(self):

        super().__init__(service=Service(ChromeDriverManager().install()))

        self.parent_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
        self.db_path = os.path.join(self.parent_dir, SQLITE_DATABASE)

        self.connection = sqlite3.connect(self.db_path)
        self.c = self.connection.cursor()


    def landing_page(self, file):

        # iktisat = economy

        path = os.path.join(main_path, file)
        abs_path = f'file:///{os.path.abspath(path)}'
        print(abs_path)
        self.get(abs_path)
        time.sleep(3)
    
    def landing_page_endistüriyel_tasarım(self):

        # endistüriyel tasarım = industrial design

        path = os.path.join(main_path, '1.endistüriyel tasarım_files',
                             'start(1).html')
        abs_path = f'file:///{os.path.abspath(path)}'
        print(abs_path)
        self.get(abs_path)
        time.sleep(3)

    def landing_page_arapça_mütercim_tercümanlık(self):

        # arapça mütercim tercümanlık = Arabic translation and interpretation

        path = os.path.join(main_path, '1.sınıf arapça mütercim tercümanlık_files',
                             'start.html')
        abs_path = f'file:///{os.path.abspath(path)}'
        print(abs_path)
        self.get(abs_path)
        time.sleep(3)

    def landing_page_2_arapça_mütercim_tercümanlık(self):

        # arapça mütercim tercümanlık = Arabic translation and interpretation

        path = os.path.join(main_path, '2.sınıf arapça mütercim tercümanlık_files',
                             'start.html')
        abs_path = f'file:///{os.path.abspath(path)}'
        print(abs_path)
        self.get(abs_path)
        time.sleep(3)

    def landing_page_3_arapça_mütercim_tercümanlık(self):

        # arapça mütercim tercümanlık = Arabic translation and interpretation

        path = os.path.join(main_path, '3.sınıf arapça mütercim tercümanlık_files',
                             'start.html')
        abs_path = f'file:///{os.path.abspath(path)}'
        print(abs_path)
        self.get(abs_path)
        time.sleep(3)

    def landing_page_4_arapça_mütercim_tercümanlık(self):

        # arapça mütercim tercümanlık = Arabic translation and interpretation

        path = os.path.join(main_path, '4.sınıf arapça mütercim tercümanlık_files',
                             'start.html')
        abs_path = f'file:///{os.path.abspath(path)}'
        print(abs_path)
        self.get(abs_path)
        time.sleep(3)

    def create_faculty_code(self, string11, string2, string3):

        result = '{}_{}@{}'.format(string11, string2, string3)
        return result
    
    def start_end_times(self, info):

        point = str(info).find('-')

        start_time = info[:point]
        end_time = info[(point+1):]

        return [start_time, end_time]
    
    def find_course_year(self, info):

        year = info[-3]
        year = int(year)
        return year
    
    def clean_code(self, info):

        point = str(info).find('(')
        code = info[:point]

        return code
    
    def clean_teacher(self, info):

        cleaned_text = re.sub(r"\b(Dr\.|Öğr\. Üyesi|Öğr\.Gör\.Dr\.|Prof\.Dr\.|Doç\.)\s*", "", info, flags=re.IGNORECASE)
        
        return cleaned_text


    def get_data(self):

        logs = open('logs.txt', 'a', encoding='utf-8')

        self.connection = sqlite3.connect(self.db_path)
        self.c = self.connection.cursor()

        table_counter = 0
        row_counter = 0

        faculty_name = self.find_element(By.ID, 'lblHeader2')
        faculty_name_text = faculty_name.get_attribute('innerText')
        print(f'the faculty name is {faculty_name_text}')
        logs.write(f'the faculty name is {faculty_name_text}\n')

        days = ['Pazartesi', 'Salı', 'Çarşamba', 'Perşembe', 'Cuma']

        all_tables = self.find_elements(By.TAG_NAME, 'tbody')
        tables = all_tables[4:]
        print(f'the num of tables = {len(tables)}')
        logs.write(f'the num of tables = {len(tables)}\n')

        day_counter = 0

        for table in tables:
            table_rows = table.find_elements(By.TAG_NAME, 'tr')


            for row in table_rows:
                course_info_list = []

                tds = row.find_elements(By.TAG_NAME, 'td')

                for td in tds:

                    td_info = td.get_attribute('innerText')
                    #print(td_info)
                    course_info_list.append(td_info)

                print(f'row info = {course_info_list}')
                logs.write(f'row info = {course_info_list}\n')
                print(f'the length of the list is {len(course_info_list)}')
                logs.write(f'the length of the list is {len(course_info_list)}\n')

                if len(course_info_list) > 1:

                    course_code = course_info_list[1]

                    course_code = self.clean_code(course_code)

                    #print(code_placeholder)

                    start_end_info = self.start_end_times(course_info_list[0])
                    start_time = start_end_info[0]
                    end_time = start_end_info[1]
                    print(f'the course starts at {start_time} and ends at {end_time}')
                    logs.write(f'the course starts at {start_time} and ends at {end_time}\n')

                    faculty_code = self.create_faculty_code(faculty_name_text, course_code, start_time)
                    print(faculty_code)
                    logs.write(faculty_code + '\n')
                    
                    course_name = course_info_list[2]
                    course_class = course_info_list[3]
                    course_teacher = course_info_list[4]

                    course_teacher = self.clean_teacher(course_teacher)

                    course_year = self.find_course_year(course_code)
                    course_day = days[day_counter]
                    print(course_day)
                    logs.write(course_day + '\n')
                    
                    try:

                        self.c.execute(f"INSERT INTO course_info VALUES (?,?,?,?,?,?,?,?,?,?,?)", (faculty_code, faculty_name_text, course_code, course_name,
                              course_class, course_teacher, course_year, course_day,
                              start_time, end_time, None,))
                        
                        self.connection.commit()
                        
                        print('it worked out!!!!')
                        logs.write('it worked out!!!!\n')

                    except :
                        """
                        # PROBLEM: it doesnt work because the primary key already exists
                        # SOLUTION: will add the start time in the faculty code
                        # then i will merge all instances of the course with the
                        # earliest start time and the latest end time
                        # then i will update the primary key with only the faculty code
                        """
                        print('didnt work out!!!')
                        logs.write('didnt work out!!!\n')
                    
                    


                else:
                    # TODO: figure out what you want to do if there are no courses on this day 
                    pass

            

                """
                info = row.get_attribute('innerText')
                print(info)
                print(type(info))
                print(len(info))

                #first_space = info.find(" ")
                #print(first_space)
                """

                row_counter = row_counter+1
                print(f'row counter = {row_counter} / {len(table_rows)}')
                logs.write(f'row counter = {row_counter} / {len(table_rows)}\n')
                time.sleep(2)

        
            time.sleep(3)
            row_counter = 0
            table_counter = table_counter + 1
            day_counter = day_counter + 1
            print(f'table counter = {table_counter}')
            logs.write(f'table counter = {table_counter}\n')
            print(f'day counter = {day_counter}')
            logs.write(f'day counter = {day_counter}\n')
            print('----------------------------------------------')
            logs.write('----------------------------------------------\n')

        table_counter = 0
        print(f'done = {table_counter}')
        logs.write(f'done = {table_counter}\n')
        logs.close()

        self.connection.close()

        time.sleep(3)