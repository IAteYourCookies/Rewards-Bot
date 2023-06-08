from User import User
import sqlite3
import time
import random
import string
import subprocess

from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

def get_random_string(length):
    # choose from all lowercase letter
    letters = string.ascii_lowercase
    numbers = string.digits
    lettuce = letters +  numbers
    result_str = ''.join(random.choice(lettuce) for i in range(length))
    return result_str





def PrintCreatedUser():
    print("Username: " + CurrentUser.Username)
    print("Password: " + CurrentUser.Password)
    print("Email:    " + CurrentUser.Email)
    print("Points:   ", end="")
    print(CurrentUser.Points)
    print("Created:   ", end="")
    print(CurrentUser.Created)

def createAccount():
    PrintCreatedUser()
    global c
    global browser
    browser.get("https://oprewards.com/login#create")

    element_email = browser.find_element(By.ID, "reg-email")
    element_username = browser.find_element(By.ID, "reg-username")
    element_password = browser.find_element(By.ID, "reg-password")
    element_repeat_password = browser.find_element(By.ID, "reg-repeat-password")
    element_security_check = browser.find_element(By.ID, "reg-bot-sum")
    element_security_check_text_raw = browser.find_element(By.XPATH, "//label[contains(text(),'Security Check:')]").text
    element_register_button = browser.find_element(By.ID, "btn-register")

    def getNumber1():
        if (repr(element_security_check_text_raw).__contains__("u200d1")):
            return 1
        else:
            if (repr(element_security_check_text_raw).__contains__("u200d2")):
                return 2
            else:
                if (repr(element_security_check_text_raw).__contains__("u200d3")):
                    return 3
                else:
                    if (repr(element_security_check_text_raw).__contains__("u200d4")):
                        return 4
                    else:
                        if (repr(element_security_check_text_raw).__contains__("u200d5")):
                            return 5
                        else:
                            if (repr(element_security_check_text_raw).__contains__("u200d6")):
                                return 6
                            else:
                                if (repr(element_security_check_text_raw).__contains__("u200d7")):
                                    return 7
                                else:
                                    if (repr(element_security_check_text_raw).__contains__("u200d8")):
                                        return 8
                                    else:
                                        if (repr(element_security_check_text_raw).__contains__("u200d9")):
                                            return 9

    def getNumber2():
        if (repr(element_security_check_text_raw).__contains__("u200c1")):
            return 1
        else:
            if (repr(element_security_check_text_raw).__contains__("u200c2")):
                return 2
            else:
                if (repr(element_security_check_text_raw).__contains__("u200c3")):
                    return 3
                else:
                    if (repr(element_security_check_text_raw).__contains__("u200c4")):
                        return 4
                    else:
                        if (repr(element_security_check_text_raw).__contains__("u200c5")):
                            return 5
                        else:
                            if (repr(element_security_check_text_raw).__contains__("u200c6")):
                                return 6
                            else:
                                if (repr(element_security_check_text_raw).__contains__("u200c7")):
                                    return 7
                                else:
                                    if (repr(element_security_check_text_raw).__contains__("u200c8")):
                                        return 8
                                    else:
                                        if (repr(element_security_check_text_raw).__contains__("u200c9")):
                                            return 9

    #print(repr(element_security_check_text_raw))


    for letters in email:
        time.sleep(random.uniform(0.01,0.03))
        element_email.send_keys(letters)

    for letters in username:
        time.sleep(random.uniform(0.01,0.03))
        element_username.send_keys(letters)

    for letters in password:
        time.sleep(random.uniform(0.01,0.03))
        element_password.send_keys(letters)

    for letters in password:
        time.sleep(random.uniform(0.01,0.03))
        element_repeat_password.send_keys(letters)

    time.sleep(random.uniform(0.01,0.03))

    element_security_check.send_keys(getNumber1()+getNumber2())

    time.sleep(random.uniform(0.01, 0.03))

    element_register_button.click()

    time.sleep(3)

    if "registered too many times" in browser.page_source:
        print('Registered too many times')
    else:
        print('Sucess!')
        c.execute("INSERT INTO User VALUES (NULL,:Username,:Password,:Email,:Points,:Created)",
                  {'Username': CurrentUser.Username, 'Password': CurrentUser.Password, 'Email': CurrentUser.Email,
                   'Points': CurrentUser.Points, 'Created': CurrentUser.Created})
        conn.commit()

    #element_register_sucess = browser.find_elements(By.CLASS_NAME, "help-inline text-error")
    #help-inline text-error
    #alert alert-success
    #print(element_register_sucess)

    #if element_register_sucess:
    #    print("Exists")
    #else:
    #    print("Doesnt Exist")






    time.sleep(1)

def loginOp(pUserID):
    global c
    global browser
    browser.get("https://oprewards.com/login")

    element_password = browser.find_element(By.ID, "login-password")
    element_username = browser.find_element(By.ID, "login-username")
    login_button = browser.find_element(By.ID, "btn-login")

    for letters in c.execute("Select Username from User WHERE UserID == :UserIDinput", {'UserIDinput': pUserID}):
        time.sleep(random.uniform(0.01,0.03))
        element_username.send_keys(letters)

    for letters in c.execute("Select Password from User WHERE UserID == :UserIDinput", {'UserIDinput': pUserID}):
        time.sleep(random.uniform(0.01, 0.03))
        element_password.send_keys(letters)

    time.sleep(0.5)
    login_button.click()
    time.sleep(3)

def earnOp():
    earn_tab_button = browser.find_element(By.XPATH, "//ul[@id='navigation']//a[normalize-space()='Earn Points']")
    earn_tab_button.click()
    time.sleep(3)
    earn_subscribe_tab = browser.find_element(By.ID, "69")
    earn_subscribe_tab.click()
    time.sleep(2)
    lootxYtChannel = browser.find_element(By.XPATH, "//h5[normalize-space()='2 points']")
    lootxYtChannel.click()
    browser.switch_to.window(browser.window_handles[1])
    time.sleep(0.5)
    browser.close()
    time.sleep(2)
    browser.switch_to.window(browser.window_handles[0])
    earn_subscribe_tab = browser.find_element(By.ID, "69")
    earn_subscribe_tab.click()
    time.sleep(2)
    lootxTwitter = browser.find_element(By.XPATH, "//h5[normalize-space()='1 point']")
    lootxTwitter.click()
    browser.switch_to.window(browser.window_handles[1])
    time.sleep(0.5)
    browser.close()
    browser.switch_to.window(browser.window_handles[0])
    time.sleep(0.5)
    browser.close()


def loginX(pUser):
    global browser
    browser.get("https://LootX.com/login")

    element_username = browser.find_element(By.ID, "login-username")
    element_password = browser.find_element(By.ID, "login-password")
    element_login_button = browser.find_element(By.ID, "btn-login")

    for letters in pUser:
        time.sleep(random.uniform(0.01,0.03))
        element_username.send_keys(letters)

    for letters in password:
        time.sleep(random.uniform(0.01, 0.03))
        element_password.send_keys(letters)

    time.sleep(0.5)
    element_login_button.click()
    time.sleep(3)

def earnX():
    earn_tab_button = browser.find_element(By.XPATH, "//a[@class='btn btn-block btn-lg btn-primary'][normalize-space()='Earn Points']")
    earn_tab_button.click()
    time.sleep(1)
    open_subscribe_tab = browser.find_element(By.ID, "open_subscribe_id")
    open_subscribe_tab.click()
    time.sleep(1)
    AlienbaumYtChannel = browser.find_element(By.XPATH, "(//span[@class='badge badge-primary points-badge'][normalize-space()='2 POINTS'])[1]")
    AlienbaumYtChannel.click()
    browser.switch_to.window(browser.window_handles[1])
    time.sleep(0.5)
    browser.close()
    time.sleep(1)
    browser.switch_to.window(browser.window_handles[0])
    LootXDiscord = browser.find_element(By.XPATH, "(//span[@class='badge badge-primary points-badge'][normalize-space()='2 POINTS'])[2]")
    LootXDiscord.click()
    browser.switch_to.window(browser.window_handles[1])
    time.sleep(0.5)
    browser.close()

for j in range(0, 1):
    # Can only create 5 accounts
    for i in range(0, 5):
        conn = sqlite3.connect('Oprewards-LootX.db')

        c = conn.cursor()

        username = get_random_string(30)
        password = get_random_string(30)
        email = get_random_string(25) + "@gmail.com"
        points = 2
        created = time.time()

        CurrentUser = User(username, password, email, points, created)

        # ------------------------------------------------------

        service_object_name = Service('C:/Users/username/Desktop/Oprewards-LootX/chromedriver.exe.exe')
        options_name = webdriver.ChromeOptions()
        options_name.add_experimental_option("detach", True)
        options_name.add_argument("--start-maximized")
        options_name.add_argument("--incognito")
        browser = webdriver.Chrome(service=service_object_name, options=options_name)
        # browser.get("https://oprewards.com/login")

        print("Try ",end="")
        print(i + 1)
        createAccount()

        if "registered too many times" in browser.page_source:
            browser.close()
            break

        browser.close()


    #subprocess.call(["C:/Users/username/Desktop/Oprewards-LootX/vpn.exe"])

#loginOp(15)
#browser.close()
#exit()
