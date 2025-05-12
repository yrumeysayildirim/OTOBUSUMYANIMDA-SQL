import pytest
from unittest.mock import MagicMock, call
from selenium.webdriver.common.by import By
from data_collections.aybu_obs_html_scraper import obs_html_scraper
import sqlite3
import time
import os
import re

@pytest.fixture
def mock_uninitialized_scraper_obs(mocker):
    os_join_results = {}
    module_main_path_args = ('data_collections','obs_html')
    os_join_results[module_main_path_args] = '/mock/data_collections/obs_html'

    mock_parent_dir = '/abs_mock/mock/parent_dir'
    fixture_db_path_args = (mock_parent_dir, 'SQLITE_DATABASE')
    os_join_results[fixture_db_path_args] = '/mock/parent_dir/SQLITE_DATABASE'


    def specific_os_join_side_effect(*args):
        return os_join_results.get(args, '/mock/default_join/' + '/'.join(args)) 

    mock_os_path_join = mocker.patch('os.path.join', side_effect=specific_os_join_side_effect)

    mock_os_path_abspath = mocker.patch('os.path.abspath', side_effect=lambda x: '/abs_mock/' + x.lstrip('/'))

    scraper = obs_html_scraper.__new__(obs_html_scraper)

    mock_sqlite_connect = mocker.patch('sqlite3.connect')
    mock_connection = MagicMock()
    mock_cursor = MagicMock()
    mock_sqlite_connect.return_value = mock_connection
    mock_connection.cursor.return_value = mock_cursor

    mocker.patch('os.path.dirname', return_value='/fake/dir/data_collections') 
    simulated_parent_dir = mock_os_path_abspath(mock_os_path_join('/fake/dir/data_collections', '..'))

    scraper.parent_dir = simulated_parent_dir 
    scraper.db_path = mock_os_path_join(scraper.parent_dir, 'SQLITE_DATABASE')

    return scraper, mock_connection, mock_cursor, mock_os_path_join, mock_os_path_abspath



def test_get_data_extracts_and_inserts_obs(mock_uninitialized_scraper_obs, mocker):
    scraper, mock_connection, mock_cursor, mock_os_path_join, mock_os_path_abspath = mock_uninitialized_scraper_obs

    mock_faculty_el = MagicMock(get_attribute=MagicMock(return_value='Siyasal Bilgiler Fakültesi'))
    mocker.patch.object(scraper, 'find_element', return_value=mock_faculty_el)

    mock_tbodies = [MagicMock() for _ in range(5)]
    mocker.patch.object(scraper, 'find_elements', return_value=mock_tbodies)

    mock_row = MagicMock()
    mock_tbodies[4].find_elements.return_value = [mock_row] 

    mock_tds = [
        MagicMock(get_attribute=MagicMock(return_value='09:00-10:00')),
        MagicMock(get_attribute=MagicMock(return_value='COURSE101(A)')),
        MagicMock(get_attribute=MagicMock(return_value='Course Name')),  
        MagicMock(get_attribute=MagicMock(return_value='Class A')),      
        MagicMock(get_attribute=MagicMock(return_value='Prof.Dr. Teacher Name')), 
        MagicMock(get_attribute=MagicMock(return_value='Dummy data 5')), 
        MagicMock(get_attribute=MagicMock(return_value='Dummy data 6')), 
    ]
    mock_row.find_elements.return_value = mock_tds 

    mock_time_sleep = mocker.patch('time.sleep')

    mock_create_faculty_code = mocker.patch.object(scraper, 'create_faculty_code')
    mock_start_end_times = mocker.patch.object(scraper, 'start_end_times', return_value=['09:00', '10:00'])
    mock_clean_code = mocker.patch.object(scraper, 'clean_code', return_value='COURSE101')
    mock_find_course_year = mocker.patch.object(scraper, 'find_course_year', return_value=1) 

    mock_clean_teacher = mocker.patch.object(scraper, 'clean_teacher', return_value='Teacher Name')



    expected_faculty_name = mock_faculty_el.get_attribute.return_value 
    expected_cleaned_code = mock_clean_code.return_value 
    expected_start_time = mock_start_end_times.return_value[0] 
    expected_faculty_code_generated = f'{expected_faculty_name}_{expected_cleaned_code}@{expected_start_time}'
    mock_create_faculty_code.return_value = expected_faculty_code_generated


    mock_cursor.execute = MagicMock() 


    mock_connection.commit = MagicMock()

    mock_connection.close = MagicMock()

    scraper.get_data()

 
    scraper.find_element.assert_called_once_with(By.ID, 'lblHeader2')


    scraper.find_elements.assert_called_once_with(By.TAG_NAME, 'tbody')

    mock_tbodies[4].find_elements.assert_called_once_with(By.TAG_NAME, 'tr') 

    mock_row.find_elements.assert_called_once_with(By.TAG_NAME, 'td')

    for td_mock in mock_tds:
         td_mock.get_attribute.assert_called_once_with('innerText')


    mock_start_end_times.assert_called_once_with(mock_tds[0].get_attribute.return_value) 
    mock_clean_code.assert_called_once_with(mock_tds[1].get_attribute.return_value) 
    mock_find_course_year.assert_called_once_with(mock_clean_code.return_value) 

    mock_clean_teacher.assert_called_once_with(mock_tds[4].get_attribute.return_value)

  
    mock_create_faculty_code.assert_called_once_with(
        expected_faculty_name,
        expected_cleaned_code, 
        expected_start_time    
    )

    mock_time_sleep.assert_has_calls([call(2), call(3)], any_order=False)  


    expected_insert_params = (
        expected_faculty_code_generated,     
        expected_faculty_name,               
        expected_cleaned_code,              
        mock_tds[2].get_attribute.return_value, 
        mock_tds[3].get_attribute.return_value, 
        mock_clean_teacher.return_value,   
        mock_find_course_year.return_value,  
        'Pazartesi',                   
        expected_start_time,            
        mock_start_end_times.return_value[1],
        None,                                
    )

    expected_insert_query = "INSERT INTO course_info VALUES (?,?,?,?,?,?,?,?,?,?,?)"
    mock_cursor.execute.assert_called_once_with(expected_insert_query, expected_insert_params)

    mock_connection.commit.assert_called_once()

    mock_connection.close.assert_called_once()