"""
This script targets a certain job posting set below in the URL variable.  You can update this to your own specific one.
Clicks and Keys will not match up most likely as every job posting on linkedin nowadays has multiple questionnaire and
almost no two are the same.  You could put more rule exceptions but depending on how the company ask the questions and
in what order, this could get fairly huge pretty quick.  Take a look at it and feel free to grab what you want from it
and edit how you like.
"""

"""Import and install appropriate modules below."""
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

"""
Utilize this exception error below for going through all the job postings in your search criteria and ignoring the ones 
that are not easy to fill out.
"""
from selenium.common.exceptions import NoSuchElementException

# Put your own credentials here.  Ensure two factor authentification is off for linkedin.
EMAIL_ADDRESS = "PUT YOUR EMAIL ADDRESS HERE FOR LINKEDIN"
PASSWORD = "PUT YOUR PASSWORD HERE"
PHONE_NUMBER = "PUT YOUR PHONE NUMBER HERE WITHOUT THE COUNTRY CODE AND NO HYPHENS"

"""Need to install the appropriate browser driver and place .exe in accessible file."""
# Chrome driver path should reference the .exe browser driver.
chrome_driver_path = "E:\Py Code\Development\chromedriver.exe"

# Access the driver
driver = webdriver.Chrome(executable_path=chrome_driver_path)

# URL for searching linkedin with the results you want.  Make sure to include "Easy Apply" in search filter.
URL = "https://www.linkedin.com/jobs/search/?currentJobId=3272494331&f_AL=true&f_E=2&f_WT=2&keywords=python%20developer&sortBy=R"

# Open the website.
driver.get(url=URL)

# Click on "Sign In" Button.
driver.find_element(By.XPATH, "/html/body/div[1]/header/nav/div/a[2]").click()

# Sleep for 1 seconds for page to load.  Adjust as needed.
time.sleep(1)

# Input email address into email input.
driver.find_element(By.XPATH, "//*[@id='username']").send_keys(EMAIL_ADDRESS)

# Input password in password input.
driver.find_element(By.XPATH, "//*[@id='password']").send_keys(PASSWORD)

# Click sign in button.
driver.find_element(By.XPATH, "//*[@id='organic-div']/form/div[3]/button").click()

# Sleep for 2 seconds for page to load.  Adjust as needed.
time.sleep(2)

# Use this if you want to access the first job on the list.
# # Access list of available jobs and click on the first job in the list.
# driver.find_element(By.CSS_SELECTOR, ".scaffold-layout__list-container li a").click()
#
# # Sleep for 2 seconds for page to load.  Adjust as needed.
# time.sleep(2)

# Click on "Easy Apply" button.
driver.find_element(By.CSS_SELECTOR, ".jobs-apply-button--top-card button").click()

# Sleep for 2 seconds for page to load.  Adjust as needed.
time.sleep(2)

# Input phone number.  This may not always work as the table comes out in a different format and the
# phone number gets put into the first box instead of the phone number box.  Still troubleshooting this to figure it
# out.
driver.find_element(By.CSS_SELECTOR, ".display-flex input").send_keys(PHONE_NUMBER)

# Click next button.
driver.find_element(By.CSS_SELECTOR, ".display-flex button").click()

# Click next button to upload resume.  NOTE: Resume should already be on file in your linkedin account for this to work.
# I utilize to elements in the XPATH to locate this button because it shares information with other buttons.
driver.find_element(By.XPATH, "//span[@class='artdeco-button__text' and text()='Next']").click()

# Plugs a years of experience into the input box for the next page.
years_of_experience = "500"
driver.find_element(By.CSS_SELECTOR, ".display-flex input").send_keys(years_of_experience)

# Click next button.
driver.find_element(By.XPATH, "//span[@class='artdeco-button__text' and text()='Next']").click()

# Click the yes icon for work authorization.
driver.find_element(By.CSS_SELECTOR, ".display-flex label").click()

# Click "Review" Button.
driver.find_element(By.XPATH, "//span[@class='artdeco-button__text' and text()='Review']").click()

# Click "Submit application" Button.
driver.find_element(By.XPATH, "//span[@class='artdeco-button__text' and text()='Submit application']").click()



