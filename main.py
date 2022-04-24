# //pip install webdriver-manager
import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service

email_id="your email id"
password="Your-password"

chrome_driver_path="C:/Users/akash/chromedriver"

options=webdriver.ChromeOptions()
options.add_experimental_option("detach", True)
driver=webdriver.Chrome(service=Service(ChromeDriverManager().install()),options=options)

driver.get("https://www.linkedin.com/jobs/search/?f_LF=f_AL&geoId=102257491&keywords=python%20developer&location=London%2C%20England%2C%20United%20Kingdom&redirect=false&position=1&pageNum=0")
time.sleep(1)
clickable=driver.find_element(By.XPATH,'/html/body/div[1]/header/nav/div/a[2]')

clickable.click()
time.sleep(2)

email=driver.find_element(By.NAME,'session_key')
email.send_keys(email_id)

email=driver.find_element(By.NAME,'session_password')
email.send_keys(password)
sign_in=driver.find_element(By.XPATH,'//*[@id="organic-div"]/form/div[3]/button')
sign_in.click()
time.sleep(4)



apply=driver.find_element(By.LINK_TEXT,'Python engineer')
apply.click()

time.sleep(2)

click_2=driver.find_element(By.CSS_SELECTOR,'.mt5 button')
click_2.click()

phone_number=driver.find_element(By.CSS_SELECTOR,'.display-flex input')
phone_number.send_keys("7022988446")

time.sleep(2)
phone_number=driver.find_element(By.CSS_SELECTOR,'.pv4 button')
phone_number.click()

next_2=driver.find_elements(By.CSS_SELECTOR,'.pv4 button')
next_2[1].click()

next_3=driver.find_elements(By.CSS_SELECTOR,'.pv4 button')
next_3[1].click()
# for i in range(2):

# next=driver.find_element(By.ID,'ember776')
# next.click()
