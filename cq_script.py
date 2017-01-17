# import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait, Select
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
# from selenium.webdriver.common.keys import Keys


def launch_clearquest():
    driver = webdriver.Chrome()
    # driver = webdriver.phantomJS()
    driver.implicitly_wait(30)
    driver.get('http://cingetplm208pc.cloud.ge.com/cqweb/')
    loginWait = WebDriverWait(driver, 30)
    try:
        loginWait.until(EC.alert_is_present(),
                        'Timed out waiting for PA creation ' +
                        'confirmation popup to appear.')
        alert = driver.switch_to_alert()
        alert.accept()
    except TimeoutException:
        pass

    elem = driver.find_element_by_id('loginId_Id')
    elem.send_keys('gfaulconbridge')
    elem = driver.find_element_by_id('passwordId')
    elem.send_keys('654321')
    elem = driver.find_element_by_id('loginButtonId')
    elem.click()

    try:
        dbWait = WebDriverWait(driver, 3600)
        dbWait.until(EC.presence_of_element_located((By.ID, 'cqNavTree_cq.repo.cq-queryfolder:33817513@7.1.1/GETS')))
        elem = driver.find_element_by_xpath("//*[@id='cqNavTree_cq.repo.cq-queryfolder:33817513@7.1.1/GETS']/following-sibling::span[@class='dijitExpandoText']")
        elem.click()
        elem = driver.find_element_by_id('cqNavTree_cq.repo.cq-queryfolder:34034945@7.1.1/GETS')
        elem.click()
        elem = driver.find_element_by_id('cqNavTree_cq.repo.cq-query:34034947@7.1.1/GETS')
        elem.click()
        elem = driver.find_element_by_id('cqNavTree_cq.repo.cq-query:34034946@7.1.1/GETS')
        elem.click()
        # elem.send_keys("GETS : GETS Product Software Change Manager, created 10/5/01 on Oracle db \n")
        # print(elem.get_attribute('value'))
        # setAttribute(driver, elem, 'value', "GETS : GETS Product Software Change Manager, created 10/5/01 on Oracle db" )
        # print(elem.get_attribute('value'))
        # elem = driver.find_element_by_id('cqConnectSubmitButtonId')
        # elem.click()
    except TimeoutException:
        pass

    import pdb; pdb.set_trace()  # XXX BREAKPOINT
    driver.quit()

    return driver


def setAttribute(driver, element, attribute_name, value):
    driver.execute_script("arguments[0].setAttribute(arguments[1], arguements[2]);",
                          element, attribute_name, value)


def get_gets_defs():
    pass


def get_gets_scns():
    pass


def get_rmd_defs():
    pass


def get_rmd_scns():
    pass

# SSO Login
# elem = driver.find_element_by_name('username')
# elem.send_keys('210060583')
# elem = driver.find_element_by_name('password')
# elem.send_keys('adel2016phikos')
# button = driver.find_element_by_name('submitFrm')
# button.click()

launch_clearquest()
