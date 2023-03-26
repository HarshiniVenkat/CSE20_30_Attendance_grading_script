# Selenium Web Scraper for Attendance Management
Grade the students in the ta section using tesseract and selenium

This Python script uses the Selenium library to automate the process of marking attendance for students on canvas speedgrader. This can be useful for managing course attendance, where a large number of students need to be marked present or absent regularly.

Installation

Before running the script, you will need to install the following packages:  
Selenium,
Pillow (PIL),
pytesseract.  

To install these packages, run the following command:  
pip install -r requirements.txt  
or  
pip install selenium Pillow pytesseract.  


Clone or download this repository.  
Install the required packages.  
Download the chromedriver executable for your operating system and save it in the same directory as the script.   
You can download it from the official website.  
Edit the following variables in the script:  
url - the URL of the website where you want to mark attendance.  
username - your login username.  
cruzid - your login password.  
ta_name - the name of the TA who is responsible for marking attendance.  
number_of_students - the total number of students whose attendance you want to mark.  
attendance_xpath - the XPATH of the HTML element where you want to mark attendance (e.g., checkbox, radio button).  
Run the script using the following command:  
python main.py  
Note: The script uses a hardcoded XPATH to locate the HTML elements on the webpage. If the webpage structure changes, the XPATHs may need to be updated.

