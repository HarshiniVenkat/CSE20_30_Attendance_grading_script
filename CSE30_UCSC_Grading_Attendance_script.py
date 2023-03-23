from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
from PIL import Image

import pytesseract


driver=webdriver.Chrome("./chromedriver")
url=""
username=""
cruzid=""
ta_name=""
number_of_students=""
driver.get(url)
message = driver.find_element(By.ID,"username")
message.send_keys(username)
psw = driver.find_element(By.ID,"password")
psw.send_keys(cruzid)
button = driver.find_element(By.NAME, "_eventId_proceed")
button.click()

time.sleep(20)
counter=0

for i in range(number_of_students):
    driver.save_screenshot("temp.png")
    name_finder_ta=pytesseract.image_to_string(Image.open('exp2.png'))

    if(name_finder_ta.find("not have a submission for")!=-1):
        push_notif=driver.find_element(By.XPATH,"/html/body/div[3]/div[2]/div[2]/div/div[1]/div/div/section/div[2]/div[3]/div/div[3]/div[2]/div[1]/label/input")
        if(push_notif.get_attribute('value')=="0"):
            pass
        else:
            push_notif.send_keys("0")



##################        FOR INSTANCE          #####################################       
#    elif(name_finder_ta.find('Harshini')!=-1 or name_finder_ta.find('harshini')!=-1 or name_finder_ta.find('Venkataraman')!=-1 or name_finder_ta.find("venkataraman")!=-1):
    elif(name_finder_ta.find(ta_name))!=-1:

        push_notif=driver.find_element(By.XPATH,"/html/body/div[3]/div[2]/div[2]/div/div[1]/div/div/section/div[2]/div[3]/div/div[3]/div[2]/div[1]/label/input")
        #push_notif.clear()
        print(push_notif.get_attribute('value'))
        if(push_notif.get_attribute("value")=="1"):
            pass
        elif(push_notif.get_attribute("value")=="11"):
            push_notif.clear()
            push_notif.send_keys("1")
            pass
        elif(push_notif.get_attribute("value")=="111"):
            push_notif.clear()
            push_notif.send_keys("1")
            pass
        else:

            push_notif.send_keys("1")


    next_button=driver.find_element(By.XPATH,"/html/body/div[3]/div[2]/div[2]/div/div[1]/div/div/nav/form/div/div[2]/div[2]/button[2]")
    next_button.click()
    time.sleep(3)


print(counter)
driver.close()





