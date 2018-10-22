import time
import csv
import pyautogui as pa
import smtplib
import os
import random
from selenium import webdriver as wb
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email.mime.application import MIMEApplication
file=open('lms.csv','r')
reader=csv.reader(file,delimiter=',')
fileName= []
for row in reader:
    user=row[0]
    passw=row[1]
    NoofSubject=row[2]
    Emailid=row[3]
    passwrd=row[4]
    
n = int(NoofSubject)-1

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
    time.sleep(5)
    span=driver.find_element(By.XPATH, '//*[@id="inst50217"]/div[2]/a/div/span')
    Totalelem=driver.find_element(By.XPATH,'//*[@class="text_pending"]/p[1]')
    Viewedelem=driver.find_element(By.XPATH,'//*[@class="text_pending"]/p[2]')
    NotViewedelem=driver.find_element(By.XPATH,'//*[@class="text_pending"]/p[3]')
    percent = 100
    Total=Totalelem.text[-2:]
    Viewed=float(Total)*(percent/100)
    ViewdStr="Viewed:\n"+str(int(Viewed))
    NotViewed=float(Total)-Viewed
    NotViewdStr="Not Viewed:\n"+str(int(NotViewed))
    driver.execute_script('arguments[0].innerText = "100%";',span)
    #driver.execute_script("arguments[0].innerText ="+str(ViewdStr),Viewedelem)
    #driver.execute_script("arguments[0].innerText ="+str(NotViewdStr),NotViewedelem)
    pie = driver.find_element(By.XPATH, '//*[@id="inst50217"]/div[2]/a/div')
    pieString="arguments[0].setAttribute('class','c100 p100 green')"
    driver.execute_script(pieString,pie)
    Links=driver.find_elements(By.XPATH, '//*[@id="couaclist"]/a')
    for link in Links:
        driver.execute_script("arguments[0].setAttribute('class', 'completed')",link)
    ChangeImg=driver.find_elements(By.XPATH,'//*[@class="completed"]/div/img[2]')
    for changeImg in ChangeImg:
        driver.execute_script("arguments[0].setAttribute('src','http://mydy.dypatil.edu/rait/theme/image.php/essential/core/1524215314/i/caution1')",changeImg)
    imageName = str(s)+".jpg"
    pa.screenshot(imageName)

def email():
    j=0
    while(j<=int(n)):
        fileName.append(str(j)+".jpg")
        j=j+1
    print (fileName)    
    msg = MIMEMultipart()
    fromaddr = Emailid
    toaddrs  = [Emailid]
    username = Emailid
    password = passwrd
    print(password)
    for f in fileName:
        file_path = f
        attachment = MIMEApplication(open(file_path, "rb").read(), _subtype="txt")
        attachment.add_header('Content-Disposition','attachment', filename=f)
        msg.attach(attachment)
    server = smtplib.SMTP('smtp.gmail.com:587')
    server.ehlo()
    server.starttls()
    server.login(username,password)
    server.sendmail(fromaddr, toaddrs, msg.as_string())
    server.quit()

       
def launch():
    i=0
    while(i<=int(n)):
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
    email()
launch()


