import time
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.keys import Keys

import pdb

def launch_clearquest():
    browser = webdriver.Chrome()
    browser.implicitly_wait(30)
    browser.get('http://cingetplm208pc.cloud.ge.com/cqweb/')
    loginWait = WebDriverWait(browser, 10)
    try:
        loginWait.until(EC.alert_is_present(),
                                       'Timed out waiting for PA creation ' +
                                       'confirmation popup to appear.')
        alert = browser.switch_to_alert()
        alert.accept()
    except TimeoutException:
        pass

    elem = browser.find_element_by_id('loginId_Id')
    elem.send_keys('gfaulconbridge')
    elem = browser.find_element_by_id('passwordId')
    elem.send_keys('gfaulconbridge')
    elem = browser.find_element_by_id('loginButtonId')
    elem.click()

    return browser

def get_gets_defs():
    pass    

def get_gets_scns():
    pass

def get_rmd_defs():
    pass

def get_rmd_scns():
    pass

# SSO Login
# elem = browser.find_element_by_name('username')
# elem.send_keys('210060583')
# elem = browser.find_element_by_name('password')
# elem.send_keys('adel2016phikos')
# button = browser.find_element_by_name('submitFrm')
# button.click()


