from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# Initialize WebDriver
options = Options()
options.add_argument("start-maximized")
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

# Function to log in to Instagram and search the username and like post
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
    message_input = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "textarea[placeholder='Message...']")))
    message_input.send_keys(message)
    time.sleep(1)
    # Click on the send button
    send_button = driver.find_element(By.XPATH, "//button[contains(text(), 'Send')]")
    send_button.click()
    time.sleep(2)

# Credentials
username = "rangoliworld_"
password = "arusha01"

# Login to Instagram
login_to_instagram(username, password)

# Message someone
recipient_username = "bhakti_darawade"
message = "This message has been sent by an Insta bot via arusha"
send_message_to_user(recipient_username, message)

# Close the WebDriver
driver.quit()
