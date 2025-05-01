from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
#import pandas as pd
import sqlite3
from data_collections.constants import AYBUZEM_URL, SQLITE_DATABASE
import time
import os
import re



class aybuzem_scraper(webdriver.Chrome):

    def __init__(self):

        super().__init__(service=Service(ChromeDriverManager().install()))

        parent_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
        db_path = os.path.join(parent_dir, SQLITE_DATABASE)

        self.connection = sqlite3.connect(db_path)
        self.c = self.connection.cursor()


    def landing_page(self):

        self.get(AYBUZEM_URL)

        time.sleep(5)

    """
    there are 7 facultys in esenboga:

    1. İlahiyat Fakültesi
    2. İletişim Fakültesi (not opened yet, i think)
    3. İnsan ve Toplum Bilimleri Fakültesi
    4. İşletme Fakültesi
    5. Mimarlık ve Güzel Sanatlar Fakültesi
    6. Sağlık Bilimleri Fakültesi
    7. Siyasal Bilgiler Fakültesi

    """

    # isletme faculty and its departements

    def isletme_faculty(self):

        self.implicitly_wait(30)

        expand_btn = self.find_element(By.CSS_SELECTOR, 'a[href="https://aybuzem.aybu.edu.tr/course/index.php?categoryid=946"]')
        expand_btn.click()

        self.implicitly_wait(30)

        isletme_btn = self.find_element(By.CSS_SELECTOR, 'a[href="https://aybuzem.aybu.edu.tr/course/index.php?categoryid=951"]')
        isletme_btn.click()

        self.implicitly_wait(30)

    def ybs_departement(self):

        self.implicitly_wait(30)

        ybs_btn = self.find_element(By.CSS_SELECTOR, 'a[href="https://aybuzem.aybu.edu.tr/course/index.php?categoryid=1068"]')
        ybs_btn.click()

    
    def itb_departement(self):

        self.implicitly_wait(30)
        itb_btn = self.find_element(By.CSS_SELECTOR, 'a[href="https://aybuzem.aybu.edu.tr/course/index.php?categoryid=1066"]')
        itb_btn.click()

    def bus_departement(self):

        self.implicitly_wait(30)
        bus_btn = self.find_element(By.CSS_SELECTOR, 'a[href="https://aybuzem.aybu.edu.tr/course/index.php?categoryid=1064"]')
        bus_btn.click()

    def fb_departement(self):

        self.implicitly_wait(30)
        fb_btn = self.find_element(By.CSS_SELECTOR, 'a[href="https://aybuzem.aybu.edu.tr/course/index.php?categoryid=1062"]')
        fb_btn.click()

    # insan faculty and its departements

    def insan_faculty(self):

        self.implicitly_wait(30)

        expand_btn = self.find_element(By.CSS_SELECTOR, 'a[href="https://aybuzem.aybu.edu.tr/course/index.php?categoryid=946"]')
        expand_btn.click()

        self.implicitly_wait(30)

        insan_btn = self.find_element(By.CSS_SELECTOR, 'a[href="https://aybuzem.aybu.edu.tr/course/index.php?categoryid=948"]')
        insan_btn.click()

        self.implicitly_wait(30)


    def TARİH_departement(self):
        self.implicitly_wait(30)
        mu_btn = self.find_element(By.CSS_SELECTOR, 'a[href="https://aybuzem.aybu.edu.tr/course/index.php?categoryid=972"]')
        mu_btn.click()

    def PSİKOLOJİ_departement(self):
        self.implicitly_wait(30)
        mu_btn = self.find_element(By.CSS_SELECTOR, 'a[href="https://aybuzem.aybu.edu.tr/course/index.php?categoryid=973"]')
        mu_btn.click()

    def TÜRK_DİLİ_VE_EDEBİYATI_departement(self):
        self.implicitly_wait(30)
        mu_btn = self.find_element(By.CSS_SELECTOR, 'a[href="https://aybuzem.aybu.edu.tr/course/index.php?categoryid=974"]')
        mu_btn.click()

    def FELSEFE_departement(self):
        self.implicitly_wait(30)
        mu_btn = self.find_element(By.CSS_SELECTOR, 'a[href="https://aybuzem.aybu.edu.tr/course/index.php?categoryid=975"]')
        mu_btn.click()
    
    def SOSYOLOJİ_departement(self):
        self.implicitly_wait(30)
        mu_btn = self.find_element(By.CSS_SELECTOR, 'a[href="https://aybuzem.aybu.edu.tr/course/index.php?categoryid=976"]')
        mu_btn.click()

    def BİLGİ_VE_BELGE_YÖNETİMİ_departement(self):
        self.implicitly_wait(30)
        mu_btn = self.find_element(By.CSS_SELECTOR, 'a[href="https://aybuzem.aybu.edu.tr/course/index.php?categoryid=977"]')
        mu_btn.click()

    def DOĞU_DİLLERİ_VE_EDEBİYATLARI_departement(self):
        self.implicitly_wait(30)
        mu_btn = self.find_element(By.CSS_SELECTOR, 'a[href="https://aybuzem.aybu.edu.tr/course/index.php?categoryid=978"]')
        mu_btn.click()

    def MÜTERCİM_VE_TERCÜMANLIK_departement(self):
        self.implicitly_wait(30)
        mu_btn = self.find_element(By.CSS_SELECTOR, 'a[href="https://aybuzem.aybu.edu.tr/course/index.php?categoryid=979"]')
        mu_btn.click()

    # ilahiyat faculty and its departements

    def ilahiyat_faculty(self):

        self.implicitly_wait(30)

        expand_btn = self.find_element(By.CSS_SELECTOR, 'a[href="https://aybuzem.aybu.edu.tr/course/index.php?categoryid=946"]')
        expand_btn.click()

        self.implicitly_wait(30)

        ilahiyat_btn = self.find_element(By.CSS_SELECTOR, 'a[href="https://aybuzem.aybu.edu.tr/course/index.php?categoryid=967"]')
        ilahiyat_btn.click()

        self.implicitly_wait(30)

    def ilahiyat_departement(self):

        self.implicitly_wait(30)
        fb_btn = self.find_element(By.CSS_SELECTOR, 'a[href="https://aybuzem.aybu.edu.tr/course/index.php?categoryid=1026"]')
        fb_btn.click()

    # Mimarlık ve Güzel Sanatlar faculty and its departements


    def Mimarlık_ve_Güzel_Sanatlar_faculty(self):

        self.implicitly_wait(30)

        expand_btn = self.find_element(By.CSS_SELECTOR, 'a[href="https://aybuzem.aybu.edu.tr/course/index.php?categoryid=946"]')
        expand_btn.click()

        self.implicitly_wait(30)

        Mimarlık_btn = self.find_element(By.CSS_SELECTOR, 'a[href="https://aybuzem.aybu.edu.tr/course/index.php?categoryid=965"]')
        Mimarlık_btn.click()

        self.implicitly_wait(30)

    def GÖRSEL_İLETİŞİM_TASARIMI_departement(self):
        self.implicitly_wait(30)
        mu_btn = self.find_element(By.CSS_SELECTOR, 'a[href="https://aybuzem.aybu.edu.tr/course/index.php?categoryid=1020"]')
        mu_btn.click()

    def MİMARLIK_departement(self):
        self.implicitly_wait(30)
        mu_btn = self.find_element(By.CSS_SELECTOR, 'a[href="https://aybuzem.aybu.edu.tr/course/index.php?categoryid=1021"]')
        mu_btn.click()

    def ENDÜSTRİYEL_TASARIM_departement(self):
        self.implicitly_wait(30)
        mu_btn = self.find_element(By.CSS_SELECTOR, 'a[href="https://aybuzem.aybu.edu.tr/course/index.php?categoryid=1022"]')
        mu_btn.click()

    # Sağlık Bilimleri faculty and its departements

    def SAĞLIK_BİLİMLERİ_faculty(self):

        self.implicitly_wait(30)

        expand_btn = self.find_element(By.CSS_SELECTOR, 'a[href="https://aybuzem.aybu.edu.tr/course/index.php?categoryid=946"]')
        expand_btn.click()

        self.implicitly_wait(30)

        Sağlık_btn = self.find_element(By.CSS_SELECTOR, 'a[href="https://aybuzem.aybu.edu.tr/course/index.php?categoryid=956"]')
        Sağlık_btn.click()

        self.implicitly_wait(30)

    def HEMŞİRELİK_departement(self):
        self.implicitly_wait(30)
        mu_btn = self.find_element(By.CSS_SELECTOR, 'a[href="https://aybuzem.aybu.edu.tr/course/index.php?categoryid=1110"]')
        mu_btn.click()

    def FİZYOTERAPİ_VE_REHABİLİTASYON_departement(self):
        self.implicitly_wait(30)
        mu_btn = self.find_element(By.CSS_SELECTOR, 'a[href="https://aybuzem.aybu.edu.tr/course/index.php?categoryid=1111"]')
        mu_btn.click()

    def SOSYAL_HİZMET_departement(self):
        self.implicitly_wait(30)
        mu_btn = self.find_element(By.CSS_SELECTOR, 'a[href="https://aybuzem.aybu.edu.tr/course/index.php?categoryid=1112"]')
        mu_btn.click()

    def ODYOLOJİ_departement(self):
        self.implicitly_wait(30)
        mu_btn = self.find_element(By.CSS_SELECTOR, 'a[href="https://aybuzem.aybu.edu.tr/course/index.php?categoryid=1113"]')
        mu_btn.click()

    def ÇOCUK_GELİŞİMİ_departement(self):
        self.implicitly_wait(30)
        mu_btn = self.find_element(By.CSS_SELECTOR, 'a[href="https://aybuzem.aybu.edu.tr/course/index.php?categoryid=1114"]')
        mu_btn.click()

    def BESLENME_VE_DİYETETİK_departement(self):
        self.implicitly_wait(30)
        mu_btn = self.find_element(By.CSS_SELECTOR, 'a[href="https://aybuzem.aybu.edu.tr/course/index.php?categoryid=1115"]')
        mu_btn.click()

    def SAĞLIK_YÖNETİMİ_departement(self):
        self.implicitly_wait(30)
        mu_btn = self.find_element(By.CSS_SELECTOR, 'a[href="https://aybuzem.aybu.edu.tr/course/index.php?categoryid=1116"]')
        mu_btn.click()

    def DİL_VE_KONUŞMA_TERAPİSİ_departement(self):
        self.implicitly_wait(30)
        mu_btn = self.find_element(By.CSS_SELECTOR, 'a[href="https://aybuzem.aybu.edu.tr/course/index.php?categoryid=1117"]')
        mu_btn.click()

    # Siyasal Bilgiler faculty and its departements

    def SİYASAL_BİLGİLER_faculty(self):

        self.implicitly_wait(30)

        expand_btn = self.find_element(By.CSS_SELECTOR, 'a[href="https://aybuzem.aybu.edu.tr/course/index.php?categoryid=946"]')
        expand_btn.click()

        self.implicitly_wait(30)

        Siyasal_btn = self.find_element(By.CSS_SELECTOR, 'a[href="https://aybuzem.aybu.edu.tr/course/index.php?categoryid=959"]')
        Siyasal_btn.click()

        self.implicitly_wait(30)

    def İKTİSAT_departement(self):
        self.implicitly_wait(30)
        mu_btn = self.find_element(By.CSS_SELECTOR, 'a[href="https://aybuzem.aybu.edu.tr/course/index.php?categoryid=1125"]')
        mu_btn.click()

    def MALİYE_departement(self):
        self.implicitly_wait(30)
        mu_btn = self.find_element(By.CSS_SELECTOR, 'a[href="https://aybuzem.aybu.edu.tr/course/index.php?categoryid=1126"]')
        mu_btn.click()

    def SİYASET_BİLİMİ_VE_KAMU_YÖNETİMİ_departement(self):
        self.implicitly_wait(30)
        mu_btn = self.find_element(By.CSS_SELECTOR, 'a[href="https://aybuzem.aybu.edu.tr/course/index.php?categoryid=1127"]')
        mu_btn.click()

    def ULUSLARARASI_İLİŞKİLER_departement(self):
        self.implicitly_wait(30)
        mu_btn = self.find_element(By.CSS_SELECTOR, 'a[href="https://aybuzem.aybu.edu.tr/course/index.php?categoryid=1128"]')
        mu_btn.click()
















    def next_page(self):

        time.sleep(5)
        next_page = self.find_element(By.CSS_SELECTOR, 'li[data-page-number="2"]')
        next_page.click()
        print('clicked')
        time.sleep(5)

    def code_name_breaker(self, info):

        point = str(info).find('-')

        code = info[:(point-1)]
        name = info[(point+2):]

        return [code, name]
        
    def tarih_code(self, info):

        point = str(info).find(' ')

        if point != -1:

            code = info[:(point)]
            name = info[(point+1):]

            r = '{}{}'.format(code,name)

            return r
        
        else:
            pass
    
    def contains_in_order(self, substring, text):
        point = str(substring).find(' ')
        if point != -1:  # Only slice if a space exists
            substring = substring[:point]

        point2 = str(substring).find('(')
        if point2 != -1:  # Only slice if a space exists
            substring = substring[:point2]

        words = substring.split()  # Split the input phrase into words
        pattern = r'\b' + r'\s*\w*\s*'.join(map(re.escape, words)) + r'\b'  # Allow flexible spacing
        return bool(re.search(pattern, text, re.IGNORECASE))
    
    """

    def clean_code(self, info):

        point = str(info).find('(')
        code = info[:point]

        return code
    
    def clean_teacher(self, info):

        point = str(info).rfind('.')
        teacher = info[point+1:]

        return teacher

    """

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
        add departement check because tit102 and others exist in all departements with
        different teachers (may not be needed, most classes of a similar natures are online)

        SHB217 did not read for some reason

        clean the print process and make it readable
        """

        logs = open('aybuzem_logs.txt', 'a', encoding='utf-8')

        summaries = self.find_elements(By.CSS_SELECTOR, 'div[class="moreinfo"]')
        for summary in summaries:
            summary.click()
            #time.sleep(2)
            course_name_element = self.find_element(By.XPATH, '//h3[@class="coursename"]/a')
            course_name = course_name_element.get_attribute('innerText')
            print(course_name)
            logs.write(f'{course_name}\n')

            """
            for felsefe and tarih it seems like the codes differ 
            but the names are the same
            
            """


            course_code_name = self.code_name_breaker(course_name)
            code = course_code_name[0]
            code = self.tarih_code(code)
            print(f'course code = {code}')
            logs.write(f'course code = {code}\n')
            name = course_code_name[1]
            name = name.title()
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

            if (sql_course_name != None) : # and (sql_course_teacher != None) (sql_course_code != None)


                if (sql_course_name[0] == name): #and (faculty_status == True) and (sql_course_teacher[0] == course_teacher)
                    # (sql_course_code[0] == name)
                    try:

                        

                        #false/self.c.execute('UPDATE course_info SET student_nums = ? WHERE course_code = ? AND teacher = ?', (int(course_students), code, sql_course_teacher[0],))
                        #self.c.execute('UPDATE course_info SET student_nums = ? WHERE course_code = ? AND faculty = ?', (int(course_students), code, faculty[0]))
                        #self.c.execute('UPDATE course_info SET student_nums = ? WHERE course_code = ?', (int(course_students), code,))
                        self.c.execute('UPDATE course_info SET student_nums = ? WHERE course_name = ?', (int(course_students), name,))
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

        