import selenium
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

mail = ""
pass1 = ""
pass2 = ""

def register():
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument("--start-maximized")
    chrome_options.add_experimental_option("detach",True)
    driver = webdriver.Chrome(options=chrome_options)
    driver.get("https://www.reebok.cl/account-login")
    print("5")
    time.sleep(5)
    print("done")
    elem = driver.find_element_by_xpath('//button[@aria-label="Crear una cuenta"]')
    elem.click()
    print("10")
    time.sleep(10)
    print("done")
    elem = driver.find_element_by_name("firstName")
    elem.send_keys("Andres",Keys.TAB)
    elem = driver.switch_to.active_element
    elem.send_keys("Hernandez",Keys.TAB)
    elem = driver.switch_to.active_element
    elem.send_keys("11",Keys.TAB)
    elem = driver.switch_to.active_element
    elem.send_keys("07",Keys.TAB)
    elem = driver.switch_to.active_element
    elem.send_keys("1997",Keys.TAB,Keys.TAB)
    elem = driver.switch_to.active_element
    elem.send_keys(Keys.ARROW_LEFT,Keys.ARROW_RIGHT,Keys.TAB)
    elem = driver.switch_to.active_element
    elem.send_keys(mail,Keys.TAB)
    elem = driver.switch_to.active_element
    elem.send_keys(pass1,Keys.TAB,Keys.TAB)
    elem = driver.switch_to.active_element
    elem.send_keys(Keys.SPACE,Keys.RETURN)
    
    return driver



def login():
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument("--start-maximized")
    chrome_options.add_experimental_option("detach",True)
    driver = webdriver.Chrome(options=chrome_options)
    driver.get("https://www.reebok.cl/account-login")
    print("5")
    time.sleep(5)
    print("done")
    elem = driver.find_element_by_id("login-email")
    elem.send_keys(mail,Keys.TAB)
    elem = driver.switch_to.active_element
    elem.send_keys(pass1,Keys.RETURN)

    return driver


def restore():
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument("--start-maximized")
    chrome_options.add_experimental_option("detach",True)
    driver = webdriver.Chrome(options=chrome_options)
    driver.get("https://www.reebok.cl/account-login")
    print("5")
    time.sleep(5)
    print("done")
    elem = driver.find_element_by_xpath('//a[@data-auto-id="login-form-forgot-password"]')
    elem.click()
    time.sleep(2)
    elem = driver.find_element_by_xpath('//input[@data-auto-id="forgotten-password-email-field"]')
    elem.send_keys(mail)
    print(10)
    time.sleep(10)
    print("done")
    elem.send_keys(Keys.RETURN)
    
    return driver


def changepass():
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument("--start-maximized")
    chrome_options.add_experimental_option("detach",True)
    driver = webdriver.Chrome(options=chrome_options)
    driver.get("https://www.reebok.cl/account-login")
    print("5")
    time.sleep(5)
    print("done")
    elem = driver.find_element_by_id("login-email")
    elem.send_keys(mail,Keys.TAB)
    elem = driver.switch_to.active_element
    elem.send_keys(pass1,Keys.RETURN)
    print(10)
    time.sleep(10)
    print("done")
    elem = driver.find_element_by_xpath('//li[*="Datos personales"]/a')
    elem.click()
    time.sleep(5)
    elem = driver.find_element_by_xpath('//section[3]/label')
    elem.click()
    elem = driver.find_element_by_name("oldPassword")
    elem.send_keys(pass1)
    elem = driver.find_element_by_name("newPassword")
    elem.send_keys(pass2,Keys.RETURN)
        
    return pass2


def force():
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument("--start-maximized")
    chrome_options.add_experimental_option("detach",True)
    driver = webdriver.Chrome(options=chrome_options)
    driver.get("https://www.reebok.cl/account-login")
    print("5")
    time.sleep(5)
    print("done")
    elem = driver.find_element_by_id("login-email")
    elem.send_keys(mail,Keys.TAB)
    elem = driver.switch_to.active_element
    for i in range(0,100):
        elem.send_keys(i,Keys.RETURN)
        time.sleep(1)

    return driver








