import os
from pathlib import Path
from datetime import datetime

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver

BASE_URL = "https://www.saucedemo.com/"


def get_driver(headless: bool = True) -> WebDriver:

    options = Options()
    if headless:
        options.add_argument("--headless=new")
    options.add_argument("--window-size=1920,1080")
    options.add_argument("--disable-gpu")
    options.add_argument("--no-sandbox")

    driver = webdriver.Chrome(options=options)
    driver.implicitly_wait(5)
    return driver


def get_credentials():

    user = os.getenv("SAUCE_USER", "standard_user")
    pwd = os.getenv("SAUCE_PWD", "secret_sauce")
    return user, pwd


def login(driver: WebDriver, username: str, password: str):
 
    driver.get(BASE_URL)
    user_input = driver.find_element(By.ID, "user-name")
    pass_input = driver.find_element(By.ID, "password")
    login_button = driver.find_element(By.ID, "login-button")

    user_input.clear()
    user_input.send_keys(username)
    pass_input.clear()
    pass_input.send_keys(password)
    login_button.click()


def take_screenshot(driver: WebDriver, name_prefix: str = "screenshot"):

    reports_dir = Path("reports") / "screenshots"
    reports_dir.mkdir(parents=True, exist_ok=True)

    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S_%f")
    filename = reports_dir / f"{name_prefix}_{timestamp}.png"
    driver.save_screenshot(str(filename))
    
    return filename