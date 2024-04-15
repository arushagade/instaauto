from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
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

# Function to add a post
def add_post(image_path, caption):
    # Navigate to the page for adding a new post
    driver.get("https://www.instagram.com/")
    time.sleep(2)  # Let the page load

    # Click the button to add a new post
    add_post_button = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, "//a[contains(@class, 'x1i10hfl xjbqb8w x1ejq31n xd10rxx x1sy0etr x17r0tee x972fbf xcfux6l x1qhh985 xm0m39n x9f619 x1ypdohk xt0psk2 xe8uvvx xdj266r x11i5rnm xat24cr x1mh8g0r xexx8yu x4uap5 x18d9i69 xkhd6sd x16tdsg8 x1hl2dhg xggy1nq x1a2a7pz _a6hd')]")))
    add_post_button.click()

    # Handle file upload (manually or using other tools)

    # Add caption
    caption_input = driver.find_element(By.XPATH, "//textarea[contains(@class, 'XrOey')]")
    caption_input.send_keys(caption)

    # Click the button to post
    post_button = driver.find_element(By.XPATH, "//button[contains(text(), 'Post')]")
    post_button.click()

# Your Instagram credentials
username = "rangoliworld_"
password = "arusha01"

xpath = "//a[@href='https://example.com']"


# Image file path
image_path = "C:/Users/Arusha Gade/Desktop/python.jpg.jpeg"

# Caption for the post
caption = "Your caption goes here"

# Initialize Chrome WebDriver using ChromeDriverManager
chrome_options = webdriver.ChromeOptions()
#chrome_options.add_argument("--headless")  # Optional: Run in headless mode (without opening a browser window)
driver = webdriver.Chrome(ChromeDriverManager().install(), options=chrome_options, service_log_path='NUL')

# Log in to Instagram
login(username, password)

# Add a post
add_post(image_path, caption)

# Close the browser
driver.quit()
