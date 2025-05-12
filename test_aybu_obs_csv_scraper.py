import pytest
from unittest.mock import MagicMock, call
from selenium.webdriver.common.by import By
from data_collections.aybu_obs_csv_scraper import csv_scraper 


import sqlite3
import time
import os
import re

@pytest.fixture
def mock_uninitialized_scraper(mocker):

    scraper = csv_scraper.__new__(csv_scraper)

    mock_sqlite_connect = mocker.patch('sqlite3.connect')
    mock_connection = MagicMock()
    mock_cursor = MagicMock()
    mock_sqlite_connect.return_value = mock_connection
    mock_connection.cursor.return_value = mock_cursor

    mock_os_path_join = mocker.patch('os.path.join', return_value='/mock/db/path.db')
    mock_os_path_abspath = mocker.patch('os.path.abspath')
    mock_os_path_abspath.return_value = '/mock/data_collections/some_file.html'

    scraper.connection = mock_connection
    scraper.c = mock_cursor
    scraper.parent_dir = '/mock/parent_dir'
    scraper.db_path = '/mock/db/path.db'   

    return scraper, mock_connection, mock_cursor, mock_os_path_join, mock_os_path_abspath


def test_landing_page_loads_file(mock_uninitialized_scraper, mocker):

    scraper, _, _, mock_os_path_join, mock_os_path_abspath = mock_uninitialized_scraper


    mock_get = mocker.patch.object(scraper, 'get')
    mock_time_sleep = mocker.patch('time.sleep')

    file_name = 'example_schedule.html'

    scraper.landing_page(file_name)

    mock_os_path_join.assert_any_call('data_collections', file_name)
    assert mock_os_path_abspath.call_args == call(mock_os_path_join.return_value)

    expected_abs_path = mock_os_path_abspath.return_value
    mock_get.assert_called_once_with(f'file:///{expected_abs_path}')

    mock_time_sleep.assert_called_once_with(3)

def test_get_data_extracts_and_inserts(mock_uninitialized_scraper, mocker):
    scraper, mock_connection, mock_cursor, _, _ = mock_uninitialized_scraper

    mock_row = MagicMock()
    mocker.patch.object(scraper, 'find_elements', return_value=[mock_row])

  
    mock_tds_corrected = [
        MagicMock(get_attribute=MagicMock(return_value='Faculty Name')), 
        MagicMock(get_attribute=MagicMock(return_value='1. Year')),      
        MagicMock(get_attribute=MagicMock(return_value='Monday')),       
        MagicMock(get_attribute=MagicMock(return_value='09:00-10:00')), 
        MagicMock(get_attribute=MagicMock(return_value='COURSE101')),   
        MagicMock(get_attribute=MagicMock(return_value='Dr. Teacher')),  
        MagicMock(get_attribute=MagicMock(return_value='Dummy Teacher')), 
        MagicMock(get_attribute=MagicMock(return_value='Dummy Class')),  
    ]
    mock_row.find_elements.return_value = mock_tds_corrected 

    mocker.patch('time.sleep')

    mock_create_faculty_code = mocker.patch.object(scraper, 'create_faculty_code')
    mock_start_end_times = mocker.patch.object(scraper, 'start_end_times', return_value=['09:00', '10:00'])
    mock_find_course_year = mocker.patch.object(scraper, 'find_course_year', return_value=1)
   
    expected_faculty_from_td = mock_tds_corrected[0].get_attribute.return_value 
    expected_code_from_td = mock_tds_corrected[4].get_attribute.return_value 
    expected_start_time_from_helper = mock_start_end_times.return_value[0] 
    expected_faculty_code_generated = f'{expected_faculty_from_td}_{expected_code_from_td}@{expected_start_time_from_helper}'
    mock_create_faculty_code.return_value = expected_faculty_code_generated


    mock_cursor.execute = MagicMock()


    mock_connection.commit = MagicMock()

    mock_log_file = MagicMock()
    mock_log_file.__enter__.return_value = mock_log_file
    mock_log_file.__exit__.return_value = None 
    mocker.patch('builtins.open', return_value=mock_log_file)


    scraper.get_data()

    scraper.find_elements.assert_called_once_with(By.TAG_NAME, 'tr')

    mock_row.find_elements.assert_called_once_with(By.TAG_NAME, 'td')


    for td_mock in mock_tds_corrected:
         td_mock.get_attribute.assert_called_once_with('innerText')


    mock_start_end_times.assert_called_once_with(mock_tds_corrected[3].get_attribute.return_value) # Called with '09:00-10:00'
    mock_find_course_year.assert_called_once_with(mock_tds_corrected[1].get_attribute.return_value) # Called with '1. Year'
    
    mock_create_faculty_code.assert_called_once_with(
        expected_faculty_from_td, 
        expected_code_from_td,   
        expected_start_time_from_helper 
    )


    expected_insert_params_actual_code_logic = (
        expected_faculty_code_generated,     
        expected_faculty_from_td,            
        expected_code_from_td,               
        mock_tds_corrected[5].get_attribute.return_value, 
        None,                              
        None,                               
        mock_find_course_year.return_value, 
        mock_tds_corrected[2].get_attribute.return_value, 
        mock_start_end_times.return_value[0],
        mock_start_end_times.return_value[1],
        None,                                
    )



    expected_insert_query = "INSERT INTO course_info VALUES (?,?,?,?,?,?,?,?,?,?,?)"
    mock_cursor.execute.assert_called_once_with(expected_insert_query, expected_insert_params_actual_code_logic)

    mock_connection.commit.assert_called_once()

    mock_connection.close.assert_called_once()

