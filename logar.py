from time import sleep 
import undetected_chromedriver as uc
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import NoSuchElementException, TimeoutException
import json
import pyautogui
from bs4 import BeautifulSoup
from selenium.webdriver.common.keys import Keys

config = json.load(open("./config.json"))

def iniciar_chrome():
    options = webdriver.ChromeOptions()
    options.add_argument("--profile-directory=Default")
    options.add_argument("--disable-infobars")
    options.add_argument("--disable-logging")
    options.add_argument("--disable-login-animations")
    options.add_argument("--disable-notifications")
    options.add_argument("--disable-default-apps")
    options.add_argument("--disable-popup-blocking")
    driver = webdriver.Chrome(options=options, executable_path=r"./chromedriver.exe")
    return driver

def logando():
    driver = uc.Chrome()
    driver.get("https://www.linkedin.com/uas/login?session_redirect=https%3A%2F%2Fwww%2Elinkedin%2Ecom%2Ffeed%2F&fromSignIn=true&trk=cold_join_sign_in")
    sleep(5)
    email = driver.find_element(By.ID,'username')
    email.send_keys(config["login"]["username"])
    sleep(0.5)
    password = driver.find_element(By.ID,'password')
    password.send_keys(config["login"]["password"])
    sleep(0.5)
    logar = driver.find_element(By.CSS_SELECTOR,'button.btn__primary--large[aria-label="Entrar"]')
    logar.click()
    print("CONTA LOGADA!!")
    sleep(6)
    cargo = driver.find_element(By.CLASS_NAME,"search-global-typeahead__input")
    cargo.send_keys(config["login"]["cargo"])
    sleep(1)
    cargo.send_keys(Keys.ENTER)
    sleep(5)
    element_li = driver.find_element(By.CLASS_NAME,"search-reusables__primary-filter")
    element_button = element_li.find_element(By.XPATH,".//button[contains(@class, 'search-reusables__filter-pill-button') and contains(text(), 'Pessoas')]")
    element_button.click()
    sleep(1000)

logando()
