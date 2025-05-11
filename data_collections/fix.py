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


def scrape(self):

    pages = self.find_elements(By.CLASS_NAME, 'page-link')
    pages_amount = int(((len(pages)/2)-1))
    print(pages_amount)

    num_clicks = pages_amount - 1
    pages_counter = 0

    
    while pages_counter < pages_amount:

        self.implicitly_wait(30)
        self.courses_loop()
        self.implicitly_wait(30)
        if pages_counter < num_clicks:
            nxt_btn = self.find_element(By.XPATH, '//a[span[text()="Next page"]]')
            nxt_btn.click()
        pages_counter = pages_counter + 1
        print(f'{pages_counter} page(s) have been done')


    #self.courses_loop()
    #self.connection.close()



"""
some may need to be edited by hand:

bf202 in bf departement

"""


def courses_loop(self):

    """
    problem: when looping through the course name the first is selected
    problem 2: the strong is it the same level as the a tag and not inside it
    
    """

    """
    PROBLEM: Some departements did not match:

    1. İNGİLİZCE MÜTERCİM VE TERCÜMANLIK / ARAPÇA MÜTERCİM VE TERCÜMANLIK (2) #

    we are going to remove the faculty check and just update where the code match
    espically that they both dont have academic english or turk dili

    2. SİY. BİL. VE KAMU YÖN. (1) #

    this is because the obs has it shortened and aybuzem has it full, we are going
    to add a condtion where if it appears faculty_status will be set to true, only tit102

    3. HEMŞİRELİK / ODYOLOJİ (2)

    some dont know why yet

    4. ÇOCUK GELİŞ, FİZYOTERAPİ,  SOSYAL HİZM (3) #

    most, even though the codes are in aybuzem (check logs)

    ÇOCUK, FİZYOTERAPİ, sql faculty no retrieve

    same for SOSYAL HİZM, problem is some course repaeat such as (SBF103),
    may just fill in by hand later

    5. İLAHİYAT, tarih, felsefe (3) #

    all for some reason, (check logs):

    ilahiyat, felsefe does not retrieve the sql_faculty for some reason

    same as .1

    TARIH may be , the faculty not retrieving, because there is a space
    in the middle in sql code, it is also not retrieving, and i also cant find 
    a single sql code in aybuzem

    """

    logs = open('fix_aybuzem_logs.txt', 'a', encoding='utf-8')

    summaries = self.find_elements(By.CSS_SELECTOR, 'div[class="moreinfo"]')
    for summary in summaries:
        summary.click()
        #time.sleep(2)
        course_name_element = self.find_element(By.XPATH, '//h3[@class="coursename"]/a')
        course_name = course_name_element.get_attribute('innerText')
        print(course_name)
        logs.write(f'{course_name}\n')


        course_code_name = self.code_name_breaker(course_name)
        code = course_code_name[0]
        print(f'course code = {code}')
        logs.write(f'course code = {code}\n')
        name = course_code_name[1]
        print(f'course name = {name}')
        logs.write(f'course name = {name}\n')

        
        self.c.execute("SELECT course_code FROM course_info WHERE course_code = (?)", (code,))
        sql_course_code  = self.c.fetchone()
        print(f'sql course code = {sql_course_code}')
        logs.write(f'sql course code = {sql_course_code}\n')

        #if not sql_course_code == None:

        #    sql_course_code = self.clean_code(sql_course_code)
        
        
        self.c.execute("SELECT course_name FROM course_info WHERE course_name = (?)", (name,))
        sql_course_name  = self.c.fetchone()

        print(f'sql course code = {sql_course_code}')
        logs.write(f'sql course code = {sql_course_code}\n')
        print(f'sql course name = {sql_course_name}')
        logs.write(f'sql course name = {sql_course_name}\n')
        
        #time.sleep(2)
        course_teacher_element = self.find_element(By.XPATH, '//li[strong[text()="Teacher:"]]/a')
        course_teacher = course_teacher_element.get_attribute('innerText')
        print(f'course teacher = {course_teacher}')
        logs.write(f'course teacher = {course_teacher}\n')
        
        self.c.execute("SELECT teacher FROM course_info WHERE course_code = ? AND course_name = ?", (code, name,))
        sql_course_teacher  = self.c.fetchone()

        course_faculty_element = self.find_element(By.XPATH, '//a[@aria-current="page"]')
        course_faculty = course_faculty_element.get_attribute('innerText')
        print(f'course faculty = {course_faculty}')
        logs.write(f'course faculty = {course_faculty}\n')

        self.c.execute("SELECT faculty FROM course_info WHERE course_code = ? AND course_name = ?", (code, name,))
        sql_course_faculty  = self.c.fetchall()
        print(f'sql course faculty = {sql_course_faculty}')
        logs.write(f'sql course faculty = {sql_course_faculty}\n')


        

        #if not sql_course_teacher == None:

        #    sql_course_teacher = self.clean_teacher(sql_course_teacher)


        print(f'sql course teacher = {sql_course_teacher}')
        logs.write(f'sql course teacher = {sql_course_teacher}\n')
        
        #time.sleep(2)
        course_students_element = self.find_element(By.XPATH, "//li[strong[contains(text(), 'Enrolled students:')]]")
        course_students = course_students_element.text.split()[-1]
        print(f'std num = {course_students}')
        logs.write(f'std num = {course_students}\n')

        
        for faculty in sql_course_faculty:

            print(f'faculty = {str(faculty[0])} in {course_faculty}')
            logs.write(f'faculty = {str(faculty[0])} in {course_faculty}\n')
            faculty_status = self.contains_in_order(str(faculty[0]), course_faculty)
            print(f'status faculty = {faculty_status}')
            logs.write(f'status faculty = {faculty_status}\n')

            if (sql_course_code != None) : # and (sql_course_teacher != None)


                if (sql_course_code[0] == code) and (faculty_status == True): # and (sql_course_teacher[0] == course_teacher)

                    try:

                        #self.c.execute('UPDATE course_info SET student_nums = ? WHERE course_code = ? AND teacher = ?', (int(course_students), code, sql_course_teacher[0],))
                        self.c.execute('UPDATE course_info SET student_nums = ? WHERE course_code = ? AND faculty = ?', (int(course_students), code, faculty[0]))
                        self.connection.commit()
                        print('std worked!!!')
                        logs.write(f'std worked!!!\n')

                        #break

                    except:

                        print('std not worked!!!')
                        logs.write(f'std not worked!!!\n')

                    print('tried')
                    logs.write(f'tried\n')

        """
        self.c.execute("SELECT teacher FROM course_info WHERE course_code = ? AND course_name = ?", (code, name,))
        sql_course_teacher  = self.c.fetchone()

        #if not sql_course_teacher == None:

        #    sql_course_teacher = self.clean_teacher(sql_course_teacher)


        print(f'second sql course teacher = {sql_course_teacher}')
                    

        if (sql_course_code != None) and (sql_course_name != None):

            if (sql_course_code[0] == code) and (sql_course_name[0] == name) and (sql_course_teacher[0] != course_teacher):

                try:

                    self.c.execute('UPDATE course_info SET student_nums = ?, teacher = ? WHERE course_code = ?', (int(course_students), course_teacher, code,))
                    self.connection.commit()
                    print('teacher std worked!!!')
                except:

                    print('teacher std not worked!!!')

        """

        #time.sleep(2)
        summary.click()
        #time.sleep(2)
        self.execute_script("arguments[0].parentNode.removeChild(arguments[0]);", course_name_element)
        self.execute_script("arguments[0].parentNode.removeChild(arguments[0]);", course_teacher_element)
        self.execute_script("arguments[0].parentNode.removeChild(arguments[0]);", course_students_element)
        
        time.sleep(2)

        print('---------------------------------------------------------------')
        logs.write(f'---------------------------------------------------------------\n')
