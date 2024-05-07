import time

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

driver.get('https://www.cowin.gov.in/')
driver.execute_script("window.open('about:blank', '_blank')")
driver.maximize_window()
driver.switch_to.window(driver.window_handles[1])
time.sleep(5)
driver.get('https://www.cowin.gov.in/faq')
driver.maximize_window()

driver.execute_script("window.open('about:blank', '_blank')")
driver.switch_to.window(driver.window_handles[2])
time.sleep(5)
driver.get('https://www.cowin.gov.in/our-partner')
driver.quit()