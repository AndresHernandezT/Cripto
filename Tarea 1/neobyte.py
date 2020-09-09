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
    driver.get("https://www.neobyte.es/inicio-sesion?back=my-account")
    elem = driver.find_element_by_id("email_create")
    elem.send_keys(mail, Keys.RETURN)
    time.sleep(5)
    elem = driver.find_element_by_id("id_gender2")
    elem.send_keys(Keys.ARROW_LEFT, Keys.TAB)
    elem = driver.switch_to.active_element
    elem.send_keys("Andres", Keys.TAB)
    elem = driver.switch_to.active_element
    elem.send_keys("Hernandez", Keys.TAB, Keys.TAB)
    elem = driver.switch_to.active_element
    elem.send_keys(pass1, Keys.TAB)
    elem = driver.switch_to.active_element
    elem.send_keys("111", Keys.TAB)
    elem = driver.switch_to.active_element
    elem.send_keys("julio", Keys.TAB)
    elem = driver.switch_to.active_element
    elem.send_keys("1997", Keys.TAB, Keys.TAB, Keys.SPACE, Keys.RETURN)
    return driver


def login():
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument("--start-maximized")
    chrome_options.add_experimental_option("detach",True)
    driver = webdriver.Chrome(options=chrome_options)
    driver.get("https://www.neobyte.es/inicio-sesion?back=my-account")
    time.sleep(5)
    elem = driver.find_element_by_id("email")
    elem.send_keys(mail, Keys.TAB, pass1, Keys.RETURN)

    return driver

def changepass():
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument("--start-maximized")
    chrome_options.add_experimental_option("detach",True)
    driver = webdriver.Chrome(options=chrome_options)
    driver.get("https://www.neobyte.es/inicio-sesion?back=my-account")
    elem = driver.find_element_by_id("email")
    elem.send_keys(mail, Keys.TAB, pass1, Keys.RETURN)
    driver.get("https://www.neobyte.es/datos-personales")
    elem = driver.find_element_by_id("old_passwd")
    elem.send_keys(pass1, Keys.TAB)
    elem = driver.switch_to.active_element
    elem.send_keys(pass2, Keys.TAB, pass2, Keys.TAB, Keys.TAB, Keys.SPACE, Keys.RETURN)

    return driver
    
def restore():
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument("--start-maximized")
    chrome_options.add_experimental_option("detach",True)
    driver = webdriver.Chrome(options=chrome_options)
    driver.get("https://www.neobyte.es/recuperacion")
    elem = driver.find_element_by_id("email")
    elem.send_keys(mail, Keys.RETURN)

    return driver


def force():
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument("--start-maximized")
    chrome_options.add_experimental_option("detach",True)
    driver = webdriver.Chrome(options=chrome_options)
    driver.get("https://www.neobyte.es/inicio-sesion?back=my-account")
    print("5")
    time.sleep(5)
    print("done")
    elem = driver.find_element_by_id("email")
    elem.send_keys(mail,Keys.TAB)
    elem = driver.switch_to.active_element
    for i in range(0,100):
        elem.send_keys(i,Keys.RETURN)
        time.sleep(1)
        elem = driver.find_element_by_id("passwd")

    return driver



    
