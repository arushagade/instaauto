from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
import time

# Function to log in to Instagram and searching the username and liking post
def login_to_instagram(username, password):
    driver.get("https://www.instagram.com/")
    time.sleep(2)  
    # To find the username field
    username_field = driver.find_element(By.NAME, "username")
    username_field.send_keys(username)

    # To find the password field   
    password_field = driver.find_element(By.NAME, "password")
    password_field.send_keys(password)

    # Click on the login button
    login_button = driver.find_element(By.CSS_SELECTOR, "button[type='submit']")
    login_button.click()
    time.sleep(5)  # Add some delay to ensure login process completes

    #for finding the username
    driver.find_element(By.XPATH,"""/html/body/div[2]/div/div/div[2]/div/div/div[1]/div[1]/div[1]/div/div/div/div/div[2]/div[2]""").click()
    time.sleep(2)
    search=driver.find_element(By.XPATH,"""/html/body/div[2]/div/div/div[2]/div/div/div[1]/div[1]/div[1]/div/div/div[2]/div/div/div[2]/div/div/div[1]/div/div/input""")
    search.send_keys("gigihadid")
    driver.find_element(By.XPATH,"""/html/body/div[2]/div/div/div[2]/div/div/div[1]/div[1]/div[1]/div/div/div[2]/div/div/div[2]/div/div/div[2]/div/div/ul/a[1]""").click()
    time.sleep(2)

    #for following the searched username
    #driver.find_element(By.XPATH,"""/html/body/div[2]/div/div/div[2]/div/div/div[1]/div[1]/div[2]/div[2]/section/main/div/header/section/div[1]/div[2]/div/div[1]/button""").click()
    #time.sleep(2)

    #for liking the post of the user
    like_button = driver.find_element(By.XPATH,"""/html/body/div[2]/div/div/div[2]/div/div/div[1]/div[1]/div[2]/div[2]/section/main/div/div[3]/div/div[1]/div[1]/a""").click()
    time.sleep(5)
    like_button.click()
    #driver.find_element(By.XPATH,"""/html/body/div[8]/div[1]/div/div[3]/div/div/div/div/div[2]/div/article/div/div[2]/div/div/div[2]/section[1]/span[1]""").click()
    #time.sleep(1)
    
# Function to send a message to a user
def send_message_to_user(username, message):
    # Navigate to user's profile
    driver.get(f"https://www.instagram.com/{username}/")
    time.sleep(2)
    # Click on the message button
    message_button = driver.find_element(By.CSS_SELECTOR, "div[role='button']")
    message_button.click()
    time.sleep(2)
    # Wait for the message input box to be clickable
    # message_input = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "textarea[placeholder='Message...']")))
    message_input = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "div[aria-label='Message']")))
    message_input.send_keys(message)
    time.sleep(1)

    driver.find_element(By.XPATH,"""/html/body/div[6]/div[1]/div/div[2]/div/div/div/div/div[2]/div/div/div[3]/button[1]""").click()
    #send button code
    driver.find_element(By.XPATH,"""/html/body/div[2]/div/div/div[2]/div/div/div[1]/div[1]/div[2]/section/div/div/div/div[1]/div/div[2]/div/div/div/div/div/div/div[2]/div/div/div[2]/div/div/div[3]""").click()
    time.sleep(2)


# Initialize WebDriver
options = Options()
options.add_argument("start-maximized")
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

# Credentials
username = "rangoliworld_"
password = "arusha01"

# Login to Instagram
login_to_instagram(username, password)

# Message someone
recipient_username = "bhakti_darawade"
message = "This msg has beeen sent by insta bot"
send_message_to_user(recipient_username, message)