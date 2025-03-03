import os
import time
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

def set_roblosecurity_cookie(driver, roblosecurity_token):
    """
    Sets the .ROBLOSECURITY cookie in the browser session.
    
    :param driver: The WebDriver instance.
    :param roblosecurity_token: The ROBLOSECURITY token to be set.
    """
    driver.add_cookie({'name': '.ROBLOSECURITY', 'value': roblosecurity_token, 'domain': 'roblox.com'})
    driver.refresh()

def initialize_driver():
    """
    Initializes and returns a new Chrome WebDriver instance.
    
    :return: A WebDriver instance.
    """
    options = webdriver.ChromeOptions()
    return webdriver.Chrome(options=options)

def login_to_roblox(driver, roblosecurity_token, timeout=5):
    """
    Logs into Roblox using the .ROBLOSECURITY token by setting the cookie and refreshing the page.
    
    :param driver: The WebDriver instance.
    :param roblosecurity_token: The ROBLOSECURITY token to be set.
    :param timeout: Maximum wait time for the URL to change (default 5 seconds).
    :return: True if login is successful, False otherwise.
    """
    driver.get('https://www.roblox.com/')

    set_roblosecurity_cookie(driver, roblosecurity_token)

    try:
        # Wait until the URL contains "/home"
        WebDriverWait(driver, timeout).until(EC.url_contains("/home"))
        return True
    except:
        return False

def main():
    # Get ROBLOSECURITY token from environment variables
    ROBLOSECURITY = os.getenv("ROBLOSECURITY")
    if not ROBLOSECURITY:
        print("Error: .ROBLOSECURITY token is not set in the .env file.")
        return

    # Initialize the WebDriver
    driver = initialize_driver()

    # Try to log in
    if login_to_roblox(driver, ROBLOSECURITY):
        print("Successfully logged in!")
    else:
        print("Login failed.")
    
    # Close the browser
    driver.quit()

if __name__ == '__main__':
    main()