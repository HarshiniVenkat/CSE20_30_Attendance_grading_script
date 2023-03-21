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

# element_present = EC.presence_of_element_located((By.XPATH, '/html/body/div[3]/div[2]/div[2]/div/div[1]/div/div[2]/p[1]'))
# WebDriverWait(driver, 45).until(element_present)

time.sleep(20)
counter=0


for i in range(number_of_students):


    driver.save_screenshot("exp2.png")
    name_finder_ta=pytesseract.image_to_string(Image.open('exp2.png'))

    #print(name_finder_ta)
    if(name_finder_ta.find("not have a submission for")!=-1):
        push_notif=driver.find_element(By.XPATH,"/html/body/div[3]/div[2]/div[2]/div/div[1]/div/div/section/div[2]/div[3]/div/div[3]/div[2]/div[1]/label/input")
        if(push_notif.get_attribute('value')=="0"):
            pass
        #push_notif.clear()
        else:
            push_notif.send_keys("0")
            #submit_button=driver.find_element(By.XPATH,"/html/body/div[3]/div[2]/div[2]/div/div[1]/div/div/section/div[2]/div[3]/div/div[4]/form/div[4]/div[2]/button")
        #submit_button.click()
        

    elif(name_finder_ta.find(ta_name)!=-1:

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
        # submit_button=driver.find_element(By.XPATH,"/html/body/div[3]/div[2]/div[2]/div/div[1]/div/div/section/div[2]/div[3]/div/div[4]/form/div[4]/div[2]/button")
        # submit_button.click()
        # counter+=1


    next_button=driver.find_element(By.XPATH,"/html/body/div[3]/div[2]/div[2]/div/div[1]/div/div/nav/form/div/div[2]/div[2]/button[2]")
    next_button.click()
    time.sleep(3)

# /html/body/div[3]/div[2]/div[2]/div/div[1]/div/div/section/div[2]/div[3]/div/div[2]/div[1]/div[1]/label
# /html/body/div[3]/div[2]/div[2]/div/div[1]/div/div/section/div[2]/div[3]/div/div[2]/div[1]/div[1]/text()
#push_notif.click()
#push_notif.send_keys("1")
# submission= driver.find_elements(By.CSS_SELECTOR, "p")
#                                          /html/body/div[3]/div[2]/div[2]/div/div[1]/div/div[2]
# print(len(submission))
# for s in submission:
#     print(s.text)
print(counter)
driver.close()





