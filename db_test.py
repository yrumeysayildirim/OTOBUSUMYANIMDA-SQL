import sqlite3
from data_collections.constants import TEST_SQLITE_DATABASE

connection = sqlite3.connect(TEST_SQLITE_DATABASE)
c = connection.cursor()

# Null Value Check

c.execute("SELECT COUNT(*) FROM course_info WHERE course_name IS NULL;")
value1 = c.fetchall()[0]
print(f"Null Value Check: {value1[0]}")

print('----------------------------------------------')

# Create (INSERT)

try:
    c.execute("""
    INSERT INTO course_info (
        faculty_code, faculty, course_code, course_name, class,
        teacher, year, day, start_time, end_time, student_nums
    ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
    """, (
        'SCI011', 'Science', 'PHY101', 'Physics I', 'A',
        'Prof. Johnson', 2024, 'Tuesday', '10:00', '12:00', 30
    ))
    connection.commit()

    print(f'INSERTION SUCCESSFUL')

except:

    print(f'INSERTION FAILED')

print('----------------------------------------------')

# Read (SELECT)

try:
    x = "İKTİSAT_ECON102"
    c.execute("SELECT * FROM course_info WHERE faculty_code = ?", (x,))
    y = c.fetchall()
    print(f"SELECTION: {y}")

except:

    print(f'SELECTION FAILED')

print('----------------------------------------------')


# Update

try:
    c.execute("UPDATE course_info SET student_nums = 35 WHERE faculty_code = 'ENG101'")
    connection.commit()
    print(f'Student count updated successfully.')

except:

    print(f'Student count update failed.')


print('----------------------------------------------')


#### Delete

try:
    # ARAPÇA MÜTERCİM VE TERCÜMANLIK_MTA208
    # ARAPÇA MÜTERCİM VE TERCÜMANLIK_MTA212
    # change to one of the above since 210 has already been deleted.
    c.execute("DELETE FROM course_info WHERE faculty_code = 'ARAPÇA MÜTERCİM VE TERCÜMANLIK_MTA210'")
    connection.commit()
    print(f'Record deleted successfully.')

except:
    print(f'Record deletion failed.')

print('----------------------------------------------')


