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


"""


run = True

while run:

    connection = sqlite3.connect(SQLITE_DATABASE)
    c = connection.cursor()

    print('jack')

    name = input('course name?\n')
    print(name)
    std = input('number of students?\n')
    std = int(std)
    print(std)



    try:

        c.execute('UPDATE course_info SET student_nums = ? WHERE course_name = ?', (std, name,))
        connection.commit()
        connection.close()
        print('std worked!!!')


        #break

    except:

        print('std not worked!!!')

    value = input('do you want to continue? (0 yes, 1 no)\n')

    value = int(value)

    if value == 0:
        run = True

    else:
        run = False

"""
"""
import sqlite3

run = True

while run:
    connection = sqlite3.connect(SQLITE_DATABASE)
    c = connection.cursor()

    print('jack')

    name = input('course name?\n').strip()
    std_input = input('number of students?\n')

    if not std_input.isdigit():
        print("Invalid number!")
        continue

    std = int(std_input)

    try:
        result = c.execute('UPDATE course_info SET student_nums = ? WHERE course_name = ?', (std, name))
        connection.commit()
        if result.rowcount == 0:
            print('No matching course. Nothing updated.')
        else:
            print('std worked!!!')
    except Exception as e:
        print('std not worked!!!', e)
    finally:
        connection.close()

    value = input('do you want to continue? (0 yes, 1 no)\n')

    if value.strip() != '0':
        run = False


"""

connection = sqlite3.connect(SQLITE_DATABASE)
c = connection.cursor()
"""
try:
    result = c.execute('UPDATE course_info SET student_nums = ? WHERE course_code = ?', (55, 'ODY202',))
    connection.commit()
    if result.rowcount == 0:
        print('No matching course. Nothing updated.')
    else:
        print('std worked!!!')
except Exception as e:
    print('std not worked!!!', e)
finally:
    connection.close()

"""
"""

shb206 61 nope
shb208 58 nope

refuse to update no matter what

"""
try:
    c.execute('''
        UPDATE course_info
        SET student_nums = 0
        WHERE student_nums IS NULL
    ''')
    connection.commit()
    connection.close()
    print('it worked')

except Exception as e:

    print('nope', e)
