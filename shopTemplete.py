from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
import time
import sys
import os

SLEEP_SECOND = 1

browser = webdriver.Chrome()
def getshopTempleteMap(username, password):

    browser.implicitly_wait(30)
    browser.maximize_window()
    # wait = WebDriverWait(browser, 10)
    browser.get("http://new.weijuju.com/login.jsp")

    input_username = browser.find_element_by_id("signin-username")
    input_passowrd = browser.find_element_by_id("signin-password")

    input_username.send_keys(username)
    input_passowrd.send_keys(password)

    time.sleep(SLEEP_SECOND)

    submit = browser.find_element_by_id("signin-btn")
    submit.click()

    #登录完成后
    time.sleep(SLEEP_SECOND)
    browser.find_element_by_xpath('//a[text()="店铺"]').click()

    time.sleep(SLEEP_SECOND)
    browser.find_element_by_xpath('//a[text()="模板市场"]').click()

    tpl_list = browser.find_elements_by_xpath('//div[@class="tpl_item clearfix"]')
    tpl_list.


    #筛选器
    return
    time.sleep(SLEEP_SECOND)
    search_list = browser.find_elements_by_xpath('//div[@class="xcxSearchItem"]')
    print(search_list)
    for item in search_list:
        time.sleep(SLEEP_SECOND)
        print(item.text)
        root_path = os.getcwd() + '/' + item.text
        if not os.path.exists():
            os.mkdir(root_path)


if __name__ == "__main__":
    # cmd, first_arg = sys.argv
    # if first_arg is None:
    #     sys.exit(-1)
    print(os.getcwd())
    getshopTempleteMap()
