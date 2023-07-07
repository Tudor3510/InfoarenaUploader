from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import StaleElementReferenceException
import time

# Using Chrome to access web
driver = webdriver.Chrome()
# Open the website
driver.get('https://infoarena.ro/account')
# Making a waiter that will wait for all the elements to be loaded
ignored_exceptions=(NoSuchElementException,StaleElementReferenceException,)
wait = WebDriverWait(driver, 10, ignored_exceptions=ignored_exceptions)  # Maximum timeout in seconds

# Select the id box
id_box = wait.until(EC.presence_of_element_located(("id", "form_username"))) 
# Send id information
id_box.send_keys('tudorcioc5')

# Find password box
pass_box = wait.until(EC.presence_of_element_located(("id", "form_password"))) 
# Send password
pass_box.send_keys('Tzitzirikutza15')

# Find login button
login_button = wait.until(EC.presence_of_element_located(("id", "form_submit"))) 
# Click login
login_button.click()

driver.get('https://infoarena.ro/problema/adunare')

# Find file button
upload_button = wait.until(EC.presence_of_element_located(("id", "form_solution"))) 
# Click login
upload_button.send_keys('C:\\Users\\tudor\\Desktop\\InfoarenaUploader\\main.cpp');

# Choose the round drop-down menu
round_selector = driver.find_element(By.ID, 'form_round')
attempts = 0
last_time = time.time()
while attempts < 100:
    try:
        print("attempts: ", attempts)
        select = Select(round_selector)

        result = select.select_by_value('arhiva')
        print("result", result, "\n")

    except StaleElementReferenceException:
        attempts += 1
        while time.time() - last_time > attempts * 1.0:
            continue
    except:
        print("Alta eroare")

    else:
        break


# while select.f != 'Arhiva de probleme':
#     continue


# Find submit button
submit_button = wait.until(EC.presence_of_element_located(("id", "form_submit"))) 
# Click login
submit_button.click()

while(True):
    continue
