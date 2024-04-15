from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
import time
from webdriver_manager.chrome import ChromeDriverManager

# Function to login to Instagram
def login(username, password):
    driver.get("https://www.instagram.com/")
    time.sleep(2)  # Let the page load

    # Find and fill in the username and password fields
    username_field = driver.find_element(By.NAME, "username")
    password_field = driver.find_element(By.NAME, "password")
    username_field.send_keys(username)
    password_field.send_keys(password)

    # Submit the form
    password_field.send_keys(Keys.RETURN)
    time.sleep(5)  # Let the login process

# Function to like a post
def like_post(post_url):
    driver.get(post_url)
    time.sleep(2)  # Let the page load

    # Retry mechanism to locate the like button
    retries = 3
    while retries > 0:
        try:
            # Find and click the like button
            like_button = driver.find_element(By.XPATH, "//span[@aria-label='Like']")
            like_button.click()
            print("Post liked successfully!")
            break
        except NoSuchElementException:
            retries -= 1
            if retries == 0:
                print("Failed to locate the like button after retries.")
                return

    time.sleep(2)  # Let the action complete

# Your Instagram credentials
username = "your_username"
password = "your_password"

# URL of the post you want to like
post_url = "https://www.instagram.com/p/C5mY8V3OGFw/?utm_source=ig_web_copy_link&igsh=MzRlODBiNWFlZA=="

# Initialize Chrome WebDriver using ChromeDriverManager
chrome_options = webdriver.ChromeOptions()
driver = webdriver.Chrome(ChromeDriverManager().install(), options=chrome_options, service_log_path='NUL')

# Log in to Instagram
login(username, password)

# Like the post
like_post(post_url)

# Close the browser
driver.quit()
