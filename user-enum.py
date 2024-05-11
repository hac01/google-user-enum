from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
import time

def check_google_account(email):
    # Specify the path to chromedriver
    chromedriver_path = "/usr/bin/chromedriver"

    # Initialize Chrome WebDriver with chromedriver path
    service = Service(chromedriver_path)
    driver = webdriver.Chrome(service=service)

    # Open Google sign-in page
    driver.get("https://accounts.google.com/")

    # Find the email input field and enter the provided email
    email_field = driver.find_element("name", "identifier")
    email_field.send_keys(email)
    email_field.send_keys(Keys.RETURN)

    # Wait for a moment to let the page load
    time.sleep(3)

    # Check if the response contains the message "Couldn't find your Google Account"
    page_source = driver.page_source
    if "Couldn't find your Google Account" in page_source:
        print(f"{email} is not a valid user.")
    else:
        print(f"{email} is a valid user.")

    # Close the WebDriver
    driver.quit()

def main():
    # Read email from a text file
    with open("emails.txt", "r") as file:
        emails = file.readlines()

    # Iterate through each email and check its validity
    for email in emails:
        check_google_account(email.strip())

if __name__ == "__main__":
    main()
