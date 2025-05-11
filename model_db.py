from data_collections.constants import SQLITE_DATABASE_MODEL, TEST_SQLITE_DATABASE
import sqlite3

con = sqlite3.Connection(TEST_SQLITE_DATABASE)
c = con.cursor()

try:
    c.execute("DELETE FROM course_info WHERE class LIKE '%UZAKTAN%' OR class LIKE '%AYBUZEM%' OR class LIKE '%İNTERNET%' OR class LIKE '%(uzaktan)%'")
    c.execute("DELETE FROM course_info WHERE faculty_code = 'HEMŞİRELİK_ING102'")
    c.execute("DELETE FROM course_info WHERE faculty_code = 'HEMŞİRELİK_TDL102@13.50'")
    c.execute("DELETE FROM course_info WHERE faculty_code = 'HEMŞİRELİK_ING302'")
    con.commit()
    print('worked')

except Exception as e:
    print('didnt work', e)

con.close()