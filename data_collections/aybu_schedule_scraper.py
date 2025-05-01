from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from data_collections.constants import MIS_1_
from bs4 import BeautifulSoup 
import pandas as pd
import time
import os

class schedule_scraper(BeautifulSoup):

    def __init__(self, html_content):
        super().__init__(html_content, 'html.parser')


    def landing_page(self):
        info = self.find_all('td', class_ = 's1')
        print(info)

class sel_aybu_scraper(webdriver.Chrome):

    def __init__(self):
        super().__init__(service=Service(ChromeDriverManager().install()))

    def landing_page(self, file_path):
        abs_path = f"file:///{os.path.abspath(file_path)}"  # Convert to absolute path
        self.get(abs_path)  # Open the file in Chrome
        print("Loaded:", abs_path)
        time.sleep(20)

    def info_isletme(self):

        rows = self.find_elements(By.TAG_NAME, 'tr')
        first_row = self.find_element(By.CSS_SELECTOR, 'tbody tr[style="height: 20px"]')
        #print(first_row)

    
        first_row_info = []
        first_infos = first_row.find_elements(By.TAG_NAME, 'td')
        #print(first_infos)
        # problem: first row is empty
        #print(len(infos))
        for first_info in first_infos:
            
            first_ri = first_info.get_attribute('innerText')
            print(f'one o {first_ri}')
            #print(ri)
            first_row_info.append(first_ri)

        print(len(first_row_info))


        row_dataframe = pd.DataFrame(columns=first_row_info)
        print(row_dataframe)
        """

        for row in rows:
            row_info = []
            infos = row.find_elements(By.TAG_NAME, 'td')
            #print(len(infos))
            for info in infos:
                
                ri = info.get_attribute('innerText')
                #print(ri)
                row_info.append(ri)
            print(row_info)
            row_dataframe.loc[-1] = row_info
            print('---------------------')
            row_info.clear()
            #time.sleep(2)

        """

        row_dataframe.to_csv('isletme.csv', index=False)
            

    def info_political(self):

        rows = self.find_elements(By.TAG_NAME, 'tr')
        
        

        print(len(rows))
        #print(len(tds))
        #print(len(ps))
        for row in rows:
            row_info = []
            tds = row.find_elements(By.TAG_NAME, 'td')
            for td in tds:
                ps = td.find_element(By.TAG_NAME, 'p')
                info = ps.get_attribute('innerText')
                row_info.append(info)

            print(row_info)
            print('---------------------')
            row_info.clear()
            time.sleep(2)



            
            


