from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
import pandas as pd
import sqlite3
import time
import os, re
from data_collections.constants import SQLITE_DATABASE


"""

          faculty_code (make yourself),
          faculty (in html),
          course_code (in html),
          course_name (in html),
          class (in html),
          teacher (in html),
          year (edit from html),
          day (in html),
          start_time (edit from html),
          end_time (edit from html),
          student_nums (aybuzem scraper),


          NOTE: 

          STEP BY STEP:

          1. create 

"""

class csv_scraper(webdriver.Chrome):

    def __init__(self):
        super().__init__(service=Service(ChromeDriverManager().install()))

        self.parent_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
        self.db_path = os.path.join(self.parent_dir, SQLITE_DATABASE)

    def landing_page(self, file):

        path = os.path.join('data_collections', file)
        abs_path = f'file:///{os.path.abspath(path)}'
        print(abs_path)
        self.get(abs_path)
        time.sleep(3)

    def isletme_landing_page(self, file):

        path = os.path.join('data_collections', file)
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

        point = str(info).find('.')
        year = info[:point]
        year = int(year)
        return year
    
    def clean_code(self, info):

        point = str(info).find('(')
        code = info[:point]

        return code
    
    def clean_teacher(self, info):
        cleaned_text = re.sub(r"\b(Dr\.|Öğr\. Üyesi|Öğr\.Gör\.Dr\.|Prof\.Dr\.|Doç\.|Arş\.Gör\.|Öğr\.Gör\.)\s*", "", info, flags=re.IGNORECASE)
        return cleaned_text
    
    def clean_isletme_faculty(self, info):

        point = str(info).find('(')
        code = info[:point]

        return code


    
    def isletme_get_data(self):

        logs = open('isletme_csv_logs.txt', 'a', encoding='utf-8')

        self.connection = sqlite3.connect(self.db_path)
        self.c = self.connection.cursor()

        rows = self.find_elements(By.TAG_NAME, 'tr')
        print(len(rows))

        row_counter = 0

        for row in rows:
            course_info_list = []

            tds = row.find_elements(By.TAG_NAME, 'td')

            for td in tds:

                td_info = td.get_attribute('innerText')
                #print(td_info)
                if len(td_info) > 0:
                    course_info_list.append(td_info)

            print(f'row info = {course_info_list}')
            logs.write(f'row info = {course_info_list}\n')
            print(f'the length of the list is {len(course_info_list)}')
            logs.write(f'the length of the list is {len(course_info_list)}\n')

            if len(course_info_list) > 0:

                course_code = course_info_list[4]
                course_faculty = self.clean_isletme_faculty(course_info_list[0])
                course_name = course_info_list[5]
                course_class = course_info_list[7]
                course_teacher = course_info_list[6]
                course_teacher = self.clean_teacher(course_teacher)
                course_year = self.find_course_year(course_info_list[1])
                course_day = course_info_list[2]
                course_start_end = self.start_end_times(course_info_list[3])
                course_start_time = course_start_end[0]
                course_end_time = course_start_end[1]
                course_std_num = None
                course_faculty_code = self.create_faculty_code(course_faculty, course_code, course_start_time)
                print(f'code = {course_code}, faculty = {course_faculty}, faculty_code = {course_faculty_code}')
                logs.write(f'code = {course_code}, faculty = {course_faculty}, faculty_code = {course_faculty_code}\n')
                print(f'name = {course_name}, class = {course_class}, teacher = {course_teacher}, year = {course_year}')
                logs.write(f'name = {course_name}, class = {course_class}, teacher = {course_teacher}, year = {course_year}\n')
                print(f'day = {course_day}, start_time = {course_start_time}, end_time = {course_end_time}, std_num = {course_std_num}')
                logs.write(f'day = {course_day}, start_time = {course_start_time}, end_time = {course_end_time}, std_num = {course_std_num}\n')
                

                try:

                        self.c.execute(f"INSERT INTO course_info VALUES (?,?,?,?,?,?,?,?,?,?,?)", (course_faculty_code, course_faculty, course_code, course_name,
                              course_class, course_teacher, course_year, course_day,
                              course_start_time, course_end_time, course_std_num,))
                        
                        self.connection.commit()
                        
                        print('isletme csv it worked out!!!!')
                        logs.write('isletme csv it worked out!!!!\n')

                except :
                    """
                    # PROBLEM: it doesnt work because the primary key already exists
                    # SOLUTION: will add the start time in the faculty code
                    # then i will merge all instances of the course with the
                    # earliest start time and the latest end time
                    # then i will update the primary key with only the faculty code
                    """
                    print('isletme csv didnt work out!!!')
                    logs.write('isletme csv didnt work out!!!\n')

            else:

                # TODO: figure out what you want to do if there are no courses on this day 
                pass


            row_counter = row_counter+1
            print(f'row counter = {row_counter} / {len(rows)}')
            logs.write(f'row counter = {row_counter} / {len(rows)}\n')
            #time.sleep(2)
            print('***************************************************')
            logs.write('***************************************************')


        self.connection.close()
                

        

    def get_data(self):

        logs = open('csv_logs.txt', 'a', encoding='utf-8')

        self.connection = sqlite3.connect(self.db_path)
        self.c = self.connection.cursor()

        rows = self.find_elements(By.TAG_NAME, 'tr')
        print(len(rows))

        row_counter = 0

        for row in rows:
            course_info_list = []

            tds = row.find_elements(By.TAG_NAME, 'td')

            for td in tds:

                td_info = td.get_attribute('innerText')
                #print(td_info)
                if len(td_info) > 0:
                    course_info_list.append(td_info)

            print(f'row info = {course_info_list}')
            logs.write(f'row info = {course_info_list}\n')
            print(f'the length of the list is {len(course_info_list)}')
            logs.write(f'the length of the list is {len(course_info_list)}\n')

            if len(course_info_list) > 0:

                course_code = course_info_list[4]
                course_faculty = course_info_list[0]
                course_name = course_info_list[5]
                course_class = None
                course_teacher = None
                course_year = self.find_course_year(course_info_list[1])
                course_day = course_info_list[2]
                course_start_end = self.start_end_times(course_info_list[3])
                course_start_time = course_start_end[0]
                course_end_time = course_start_end[1]
                course_std_num = None
                course_faculty_code = self.create_faculty_code(course_faculty, course_code, course_start_time)
                print(f'code = {course_code}, faculty = {course_faculty}, faculty_code = {course_faculty_code}')
                logs.write(f'code = {course_code}, faculty = {course_faculty}, faculty_code = {course_faculty_code}\n')
                print(f'name = {course_name}, class = {course_class}, teacher = {course_teacher}, year = {course_year}')
                logs.write(f'name = {course_name}, class = {course_class}, teacher = {course_teacher}, year = {course_year}\n')
                print(f'day = {course_day}, start_time = {course_start_time}, end_time = {course_end_time}, std_num = {course_std_num}')
                logs.write(f'day = {course_day}, start_time = {course_start_time}, end_time = {course_end_time}, std_num = {course_std_num}\n')
                

                try:

                        self.c.execute(f"INSERT INTO course_info VALUES (?,?,?,?,?,?,?,?,?,?,?)", (course_faculty_code, course_faculty, course_code, course_name,
                              course_class, course_teacher, course_year, course_day,
                              course_start_time, course_end_time, course_std_num,))
                        
                        self.connection.commit()
                        
                        print('csv it worked out!!!!')
                        logs.write('csv it worked out!!!!\n')

                except :
                    """
                    # PROBLEM: it doesnt work because the primary key already exists
                    # SOLUTION: will add the start time in the faculty code
                    # then i will merge all instances of the course with the
                    # earliest start time and the latest end time
                    # then i will update the primary key with only the faculty code
                    """
                    print('csv didnt work out!!!')
                    logs.write('csv didnt work out!!!\n')

            else:

                # TODO: figure out what you want to do if there are no courses on this day 
                pass


            row_counter = row_counter+1
            print(f'row counter = {row_counter} / {len(rows)}')
            logs.write(f'row counter = {row_counter} / {len(rows)}\n')
            #time.sleep(2)
            print('***************************************************')
            logs.write('***************************************************')


        self.connection.close()




