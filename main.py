from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep

class LyntrBot:
    def __init__(self, token: str = None):
        """
        Initializes the LyntrBot class.

        Args:
            token (str): The authentication token for the user.
        """
        self.driver = webdriver.Chrome()  # Initialize the webdriver
        self.cookies = {
            "_TOKEN__DO_NOT_SHARE": str(token),  # Set the authentication token
        }
        self.home()  # Navigate to the homepage
        self.insert_cookies()  # Insert the authentication token into the browser

    def home(self):
        """
        Navigates to the homepage of the Lyntr website.

        This function uses the `get` method of the webdriver to navigate to
        the homepage of the Lyntr website.
        """
        # Navigate to the homepage of the Lyntr website
        self.driver.get("https://lyntr.com/")

    def insert_cookies(self):
        """
        Inserts cookies into the browser.

        This function iterates over the cookies dictionary and adds each cookie
        to the browser using the `add_cookie` method of the webdriver. After
        adding all the cookies, it waits for 5 seconds and refreshes the page.
        """
        # Iterate over the cookies dictionary
        for key, value in self.cookies.items():
            # Add the cookie to the browser
            self.driver.add_cookie({"name": key, "value": value})

        # Wait for 5 seconds
        sleep(5)

        # Refresh the page
        self.driver.refresh()

    def send_post(self, text):
        """
        Sends a post by clicking the post button, entering the text, and clicking the send button.

        Args:
            text (str): The text to be sent as a post.
        """
        # Wait until the post button is present
        wait = WebDriverWait(self.driver, 10)
        wait.until(EC.presence_of_element_located((By.XPATH, "/html/body/div[1]/div[1]/div/div/div[1]/div[1]/div[3]/button[1]")))

        # Click the post button
        self.driver.find_element(By.XPATH, "/html/body/div[1]/div[1]/div/div/div[1]/div[1]/div[3]/button[1]").click()

        # Wait until the text field is present
        wait.until(EC.presence_of_element_located((By.XPATH, "/html/body/div[3]/div[2]/div[1]/div/div/div/div[1]")))

        # Enter the text into the text field
        self.driver.find_element(By.XPATH, "/html/body/div[3]/div[2]/div[1]/div/div/div/div[1]").send_keys(text)

        # Wait until the send button is present
        wait.until(EC.presence_of_element_located((By.XPATH, "/html/body/div[3]/div[2]/div[2]/button")))

        # Click the send button
        self.driver.find_element(By.XPATH, "/html/body/div[3]/div[2]/div[2]/button").click()


if __name__ == "__main__":
    bot = LyntrBot(token="INSERT YOUR TOKEN HERE")
    bot.send_post("Hello, Lynter!")


