import pytest
from unittest.mock import MagicMock, call
from selenium.webdriver.common.by import By
from data_collections.aybu_aybuzem_webscraper import aybuzem_scraper
import sqlite3
import time
import os
import re

@pytest.fixture
def mock_uninitialized_scraper(mocker):
    scraper = aybuzem_scraper.__new__(aybuzem_scraper)

    mock_sqlite_connect = mocker.patch('sqlite3.connect')
    mock_connection = MagicMock()
    mock_cursor = MagicMock()
    mock_sqlite_connect.return_value = mock_connection
    mock_connection.cursor.return_value = mock_cursor

    mocker.patch('os.path.join', return_value='/mock/db/path.db')


    scraper.connection = mock_connection
    scraper.c = mock_cursor

    return scraper, mock_connection, mock_cursor



def test_scrape_calls_loop_and_clicks(mock_uninitialized_scraper, mocker):
    scraper, _, _ = mock_uninitialized_scraper

 
    mock_page_links = [MagicMock() for _ in range(8)]
    mocker.patch.object(scraper, 'find_elements', return_value=mock_page_links)

 
    mock_next_button = MagicMock()
    mock_next_button.click = MagicMock() 

 
    def find_element_side_effect(by, value):
        if by == By.XPATH and value == '//a[span[text()="Next page"]]':
            return mock_next_button

        return MagicMock()

    mocker.patch.object(scraper, 'find_element', side_effect=find_element_side_effect)


    mocker.patch.object(scraper, 'implicitly_wait')


    mock_courses_loop = mocker.patch.object(scraper, 'courses_loop')

    scraper.scrape()

    assert mock_courses_loop.call_count == 3

    assert mock_next_button.click.call_count == 2



def test_courses_loop_extracts_data_and_selects_db_only(mock_uninitialized_scraper, mocker):
    scraper, mock_connection, mock_cursor = mock_uninitialized_scraper 

    mock_summary_element = MagicMock()
    mock_summary_element.click = MagicMock() 
    mocker.patch.object(scraper, 'find_elements', return_value=[mock_summary_element])

    mock_course_title_el = MagicMock()
    mock_course_title_el.get_attribute.return_value = "CS101 - AI" 
    mock_teacher_el = MagicMock()
    mock_teacher_el.get_attribute.return_value = "Dr. Smith" 

    mock_students_el = MagicMock()
    mock_students_el.text = "Enrolled students: 150" 

    mock_faculty_el = MagicMock()
    mock_faculty_el.get_attribute.return_value = "Engineering Faculty"

   
    mocker.patch.object(scraper, 'find_element').side_effect = [
        mock_course_title_el, 
        mock_teacher_el,     
        mock_faculty_el,     
        mock_students_el,     

    ]

    mock_execute_script = mocker.patch.object(scraper, 'execute_script')

    mocker.patch('time.sleep')

    mock_code_name_breaker = mocker.patch.object(scraper, 'code_name_breaker', return_value=("CS101", "AI"))

    mock_tarih_code = mocker.patch.object(scraper, 'tarih_code', return_value="CS101")


    mock_contains_in_order = mocker.patch.object(scraper, 'contains_in_order', return_value=True) # Return value doesn't affect SELECTs


    mock_cursor.fetchone.side_effect = [
        ("CS101",),      
        ("Ai",),         
        ("Dr. Smith",), 
    ]


    mock_cursor.fetchall.return_value = [("Engineering",)] 

    mock_cursor.execute = MagicMock() 

    mock_connection.commit = MagicMock()

    scraper.courses_loop()


    assert mock_summary_element.click.call_count == 2

    find_element_mock = scraper.find_element
    assert find_element_mock.call_args_list == [
        call(By.XPATH, '//h3[@class="coursename"]/a'),
        call(By.XPATH, '//li[strong[text()="Teacher:"]]/a'),
        call(By.XPATH, '//a[@aria-current="page"]'),
        call(By.XPATH, "//li[strong[contains(text(), 'Enrolled students:')]]"), 
    ]

    mock_code_name_breaker.assert_called_once_with("CS101 - AI")
    mock_tarih_code.assert_called_once_with("CS101") 
    assert mock_contains_in_order.called 
    assert mock_contains_in_order.call_args_list == [call("Engineering", "Engineering Faculty")]

    mock_cursor.execute.assert_any_call("SELECT course_code FROM course_info WHERE course_code = (?)", ("CS101",))
    mock_cursor.execute.assert_any_call("SELECT course_name FROM course_info WHERE course_name = (?)", ("Ai",))
    mock_cursor.execute.assert_any_call("SELECT teacher FROM course_info WHERE course_code = ? AND course_name = ?", ("CS101", "Ai",))
    mock_cursor.execute.assert_any_call("SELECT faculty FROM course_info WHERE course_code = ? AND course_name = ?", ("CS101", "Ai",))

    assert mock_execute_script.called
