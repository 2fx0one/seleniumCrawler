from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
import time
import os
import requests

from bs4 import BeautifulSoup

browser = webdriver.Chrome()
SLEEP_SECOND = 1

def general_txt(url):
    html = requests.get(url).text
    # print(html)
    bs = BeautifulSoup(html, "lxml")
    # bs.prettify()

    # printf(bs.h1.text)
    div_html = bs.select('.art-content')[0].prettify()
    f = open(os.getcwd() + "/txt/" + bs.h1.text + ".txt", "wb")
    f.write(div_html.encode())
    f.close()

def get_info(main_url):
    print(main_url)
    browser.implicitly_wait(30)
    browser.maximize_window()
    browser.get(main_url)

    # time.sleep(SLEEP_SECOND)

    # 今日更新
    cms = browser.find_element_by_class_name('newlist')
    print(cms)
    li_arr = cms.find_elements_by_tag_name('li')
    print(li_arr)
    map(lambda x: x, li_arr)

    window_index = 0
    for item in li_arr:
        # 非广告
        if str(item.text).find("[广告]"):
            time.sleep(SLEEP_SECOND * 5)
            a = item.find_element_by_tag_name("a")
            item_title = a.get_attribute('title')
            item_url = a.get_attribute('href')
            print('标题:', item_title)
            print('url:', item_url)
            # print(item.text)
            general_txt(item_url)
            # html = requests.get(item_url).text
            # # print(html)
            # bs = BeautifulSoup(html, "lxml")
            # # bs.prettify()
            #
            # # printf(bs.h1.text)
            # div_html = bs.select('.art-content')[0].prettify()
            # f = open(os.getcwd() + "/txt/" + bs.h1.text + ".txt", "wb")
            # f.write(div_html.encode())
            # f.close()
            # break
            # item.click()
            # browser.get()
            # browser.switch_to.window(browser.window_handles[++window_index])
            # main_title = browser.find_element_by_xpath('//h1[@class="main-tit2"]')
            # print('标题：\n', main_title.text)
            # content = browser.find_element_by_xpath('//div[@class="art-content pt10 f16 lh200"]')
            # print(content.get_attribute('innerHTML'))
            #
            # # break
            #
            # # 存在网盘地址
            # if content.text.find("蓝奏网盘") == 0:
            #     down = content.find_element_by_class_name("FengDown")
            #     click_str = down.get_attribute("onclick")
            #     print(click_str)

            # browser.get(main_url)
            # browser.switch_to.window(browser.window_handles[0])
            # browser.back()
        # img = item.find_element_by_tag_name('img')
        # if img:
        #     img_src = img.get_attribute('src')
        #     print(img_src)
        # a = item.find_element_by_tag_name('a')
        # a.click()
        # item.click()
        # break


if __name__ == '__main__':
    print("hello game assistant!")
    get_info('https://678cn.com/')
