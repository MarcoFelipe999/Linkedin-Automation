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
"""
My name is Marcos and I developed a code with the aim of facilitating 
the creation of connections on LinkedIn in an automated way, 
in order to help people expand their network of contacts.
"""
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
    login = driver.find_element(By.CSS_SELECTOR,'button.btn__primary--large[aria-label="Entrar"]')
    login.click()
    print("CONTA LOGADA // LOGGED ACCOUNT")
    sleep(6)
    cargo = driver.find_element(By.CLASS_NAME,"search-global-typeahead__input")
    cargo.send_keys(config["login"]["cargo"])
    sleep(1)
    cargo.send_keys(Keys.ENTER)
    sleep(7)
    people = driver.find_element(By.XPATH,"//button[text()='Pessoas']")
    people.click()
    sleep(5)
    def conectar():
        while True:
            sleep(10)
            conectar = driver.find_elements(By.XPATH,'//span[@class="artdeco-button__text" and text()="Conectar"]')
            if conectar:
                print("FAZENDO CONEXÕES // MAKING CONNECTIONS")
                for elemento in conectar:
                    sleep(2)
                    elemento.click()
                    sleep(3)
                    try:
                        enviar = driver.find_element(By.XPATH,'//span[text()="Enviar"]/..')
                        enviar.click()
                        print("CONEXÃO ENVIADA // CONNECTION SENT") 
                    except:
                        print("CONEXÃO NÃO ENCONTRADA // CONNECTION NOT FOUND")
                        sleep(9)


            else:
                print("PRÓXIMA PÁGINA // NEXT PAGE")
                sleep(1)
                driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
                sleep(3)
                botao = driver.find_element(By.CSS_SELECTOR,"button.artdeco-pagination__button--next")
                botao.click()
    conectar()        
        
logando()
