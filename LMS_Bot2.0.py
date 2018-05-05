from selenium import webdriver as wb
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
import time
import csv
import pyautogui as pa
n = input("Enter no of subject ")
file=open('lms.csv','r')
reader=csv.reader(file,delimiter=',')
for row in reader:
    user=row[0]
    passw=row[1]

driver=wb.Firefox()
driver.maximize_window()
page=driver.get("http://mydy.dypatil.edu/")
wait = WebDriverWait(driver, 15)
driver.find_element_by_name("username").send_keys(user)
driver.find_element_by_name("next").send_keys(Keys.ENTER)
time.sleep(5)
driver.find_element_by_name("password").send_keys(passw)
driver.find_element_by_id("loginbtn").send_keys(Keys.ENTER)

def readpercent(s):
    span1=driver.find_element(By.XPATH, '//*[@id="inst50217"]/div[2]/a/div').click()
    time.sleep(7)
    span=driver.find_element(By.XPATH, '//*[@id="inst50217"]/div[2]/a/div/span')
    driver.execute_script("arguments[0].innerText = '200%'",span)
    pie = driver.find_element(By.XPATH, '//*[@id="inst50217"]/div[2]/a/div')
    driver.execute_script("arguments[0].setAttribute('class', 'c100 p24 green')",pie)
    Links=driver.find_elements(By.XPATH, '//*[@id="couaclist"]/a')
    for link in Links:
        driver.execute_script("arguments[0].setAttribute('class', 'pending')",link)
    ChangeImg=driver.find_elements(By.XPATH,'//*[@class="pending"]/div/img[2]')
    for changeImg in ChangeImg:
        driver.execute_script("arguments[0].setAttribute('src','http://mydy.dypatil.edu/rait/theme/image.php/essential/core/1524215314/i/grade_incorrect')",changeImg)
    imageName = str(s)+".jpg"
    pa.screenshot(imageName)
   
	
def launch():
    i=0
    while(i<int(n)):
        time.sleep(5)
        links=driver.find_elements_by_class_name('launchbutton')
        links[i].send_keys(Keys.CONTROL+Keys.ENTER)
        time.sleep(2)
        window_after = driver.window_handles[1]
        window_before = driver.window_handles[0]
        driver.switch_to_window(window_after)
        readpercent(i)
        driver.switch_to_window(window_before)
        i=i+1
    
launch()

