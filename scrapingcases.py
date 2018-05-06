
import requests
import selenium
from selenium import webdriver
import time
import glob
import pandas as pd

# This needs cleaning up as not all modules are used:
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

driver = webdriver.Firefox()

bvger_form = 'https://jurispub.admin.ch/publiws/?lang=de'

driver.get(bvger_form)

driver.find_element_by_id('form:tree:n-3:_id76').click()
driver.find_element_by_id('form:tree:n-4:_id76').click()

# Enter dates
fromdate = driver.find_element_by_id("form:calFrom")
fromdate.send_keys('1.1.2017')
todate = driver.find_element_by_id("form:calTo")
todate.send_keys('31.12.2017')

# Click "suchen"
driver.find_element_by_id('form:_id120').click()

time.sleep(5)

# Sort by date
driver.find_element_by_id('form:resultTable:_id43').click()

# Open the first case
driver.find_element_by_id('form:resultTable:0:_id36').click()

time.sleep(10)
# Now we should be at the first case. 

timeout = 500
# The website is slower - therefore wait until it's loaded.

for file in range(0, 3500):    
    try:
        ruling=driver.find_element_by_class_name('icePnlGrp')
        firstfile = open('txtfiles/test/' + str(file) + '.txt', 'w')
        firstfile.write(ruling.text)
        firstfile.close()
        # Not every case lists the cited statutes. Therefore try/except.
        try:
            federal_statutes = driver.find_element_by_id('_id8:_id58')
            secondfile = open('txtfiles/test/' + str(file) + 'statutes.txt', 'w')
            secondfile.write(federal_statutes.text)
            secondfile.close()
        except:
            print('No statutes. File: ' + str(file))
    
        driver.find_element_by_id('_id8:_id25').click()

        time.sleep(15)
    except:
        errorfile = open('txtfiles/test/' + str(file) + 'ERROR.txt', 'w')
        errorfile.write('Something happened here.')
        errorfile.close()


print('Done')
