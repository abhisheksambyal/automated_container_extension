from warnings import filterwarnings
from selenium import webdriver
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
# from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains

import pandas as pd
import time

option = webdriver.ChromeOptions()
# option.add_argument("-incognito")
# option.add_argument("--headless")
#option.add_argument("disable-gpu")

browser = webdriver.Chrome(executable_path='chromedriver_linux64/chromedriver', options=option) 

browser.get("https://docs.google.com/forms/d/e/1FAIpQLSelP0BWCIp34R7hDsVpcmAY6nxfIK7YZF6CnJ59lcZW99MImQ/viewform")

user_data = pd.read_csv('user_data.csv', delimiter=';')

#####################################
username = browser.find_elements_by_class_name("whsOnd")
next1 = browser.find_elements_by_class_name("VfPpkd-vQzf8d")

username[0].send_keys(user_data['email_id'])
time.sleep(3)
next1[0].click()

time.sleep(3)
password = browser.find_elements_by_class_name("whsOnd")
password[0].send_keys(user_data['password'])
time.sleep(2)

next2 = browser.find_elements_by_class_name("VfPpkd-vQzf8d")
next2[0].click()

#####################################
time.sleep(7)
textboxes = browser.find_elements_by_class_name("quantumWizTextinputPaperinputInput")
typeofrequest = browser.find_elements_by_class_name("docssharedWizToggleLabeledLabelText")
nextbutton = browser.find_elements_by_class_name("appsMaterialWizButtonEl")



dropdowns = browser.find_elements_by_class_name("quantumWizMenuPaperselectEl")

department= user_data['department'][0]
action = ActionChains(browser)
action.move_to_element(dropdowns[0]).perform()
# time.sleep(4)
dropdowns[0].click()

selectionXpath = "//div[@class='exportSelectPopup quantumWizMenuPaperselectPopup appsMaterialWizMenuPaperselectPopup']//span[@class='quantumWizMenuPaperselectContent exportContent' and text()='"+department+"']"
selection = WebDriverWait(browser, 10).until(EC.presence_of_element_located((By.XPATH, selectionXpath)))
selection.click()


supervisor = user_data['supervisor'][0]
action = ActionChains(browser)
action.move_to_element(dropdowns[1]).perform()
# time.sleep(4)
dropdowns[1].click()

selectionXpath = "//div[@class='exportSelectPopup quantumWizMenuPaperselectPopup appsMaterialWizMenuPaperselectPopup']//span[@class='quantumWizMenuPaperselectContent exportContent' and text()='"+supervisor+"']"
selection = WebDriverWait(browser, 10).until(EC.presence_of_element_located((By.XPATH, selectionXpath)))
selection.click()



urgency = user_data['urgency'][0]
action = ActionChains(browser)
action.move_to_element(dropdowns[2]).perform()
# time.sleep(4)
dropdowns[2].click()

selectionXpath = "//div[@class='exportSelectPopup quantumWizMenuPaperselectPopup appsMaterialWizMenuPaperselectPopup']//span[@class='quantumWizMenuPaperselectContent exportContent' and text()='"+urgency+"']"
selection = WebDriverWait(browser, 10).until(EC.presence_of_element_located((By.XPATH, selectionXpath)))
selection.click()



server = user_data['server'][0]
action = ActionChains(browser)
action.move_to_element(dropdowns[3]).perform()
# time.sleep(4)
dropdowns[3].click()

selectionXpath = "//div[@class='exportSelectPopup quantumWizMenuPaperselectPopup appsMaterialWizMenuPaperselectPopup']//span[@class='quantumWizMenuPaperselectContent exportContent' and text()='"+server+"']"
selection = WebDriverWait(browser, 10).until(EC.presence_of_element_located((By.XPATH, selectionXpath)))
selection.click()

# print(textboxes)
# print(len(textboxes))
# print(radiobuttons)
# print(nextbutton)

time.sleep(5)
name = textboxes[0]
rollno = textboxes[1]
research_work = textboxes[2]
uptime = textboxes[3]
ram = textboxes[4]

name.send_keys(user_data['name'])
rollno.send_keys(user_data['rollno'])
research_work.send_keys(user_data['research_work'])
uptime.send_keys(user_data['uptime'].astype("string"))
ram.send_keys(user_data['ram'].astype("string"))
typeofrequest[user_data['typeofrequest'][0]].click()

time.sleep(3)
nextbutton[0].click()

# Next page
time.sleep(10)
container_username = browser.find_elements_by_class_name("quantumWizTextinputPaperinputInput")
send_copy_to_email = browser.find_elements_by_class_name("quantumWizTogglePapertoggleThumb")
submit = browser.find_elements_by_class_name("appsMaterialWizButtonPaperbuttonLabel")[1]


# print(container_username)
# print(len(container_username))

# print(send_copy_to_email)
# print(len(send_copy_to_email))
# print(submit)

container_username[0].send_keys(user_data['containerusername'])
send_copy_to_email[0].click()
time.sleep(5)
submit.click()

print('SUBMITTED')
time.sleep(5)
browser.quit()
