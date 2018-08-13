from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys

import http.cookiejar
from urllib import request
import urllib.parse

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

    time.sleep(SLEEP_SECOND)
    # cookie = http.cookiejar.CookieJar()
    # handler = request.HTTPCookieProcessor(cookie)
    # opener = request.build_opener(handler)
    # session_id = browser.get_cookie("SHIROSESSIONID")
    # username = browser.get_cookie("username")
    # print(session_id)
    # print(username)

    # 准备把selenium 格式的 cookie   转换成urllib需要的格式
    cookie = [item['name'] + '=' + item['value'] for item in browser.get_cookies()]
    print(cookie)
    cookie_str = ';'.join(item for item in cookie)
    headers = {'cookie': cookie_str}
    print("urllib 需要的 cookie" + str(headers))

    # req1 = request.Request(url="http://new.weijuju.com/admin/config/getPreviewQrcode.do?page=pages%2Findex%2Ftpl_index&scene=tplid%3D208", headers=headers)
    # response = request.urlopen(req1)
    # f = open(os.getcwd() + "/qr.png", "wb")
    # f.write(response.read())
    # f.close()

    # 登录完成后
    time.sleep(SLEEP_SECOND)
    browser.find_element_by_xpath('//a[text()="店铺"]').click()

    time.sleep(SLEEP_SECOND)
    browser.find_element_by_xpath('//a[text()="模板市场"]').click()

    # 筛选器
    time.sleep(SLEEP_SECOND)
    search_list = browser.find_elements_by_xpath('//div[@class="xcxSearchItem"]')
    print(search_list)
    for item in search_list:
        item.click()
        time.sleep(SLEEP_SECOND)
        print(item.text)
        root_path = os.getcwd() + '/' + item.text
        if not os.path.exists(root_path):
            os.mkdir(root_path)

        # 查看该分类下物品
        for i in range(5):
            time.sleep(0.5)
            ActionChains(browser).send_keys(Keys.PAGE_DOWN).perform()

        # 鼠标移动
        tpl_list = browser.find_elements_by_xpath('//div[@class="tpl_item clearfix"]')
        for tpl in tpl_list:
            ActionChains(browser).move_to_element(tpl).perform()

        tpl_list = browser.find_elements_by_xpath('//div[@class="tpl_item clearfix"]')
        for tpl in tpl_list:
            # name = tpl.find_element_by_xpath('//div[@class="tip_div"]').text
            name = tpl.find_element_by_class_name('tip_div').text.split()[0]
            if name == "DIY模版":
                continue

            url = tpl.find_element_by_class_name('tpl_img').get_attribute("src")
            url_qr = tpl.find_element_by_class_name('qrcode_img').get_attribute("src")
            time.sleep(SLEEP_SECOND)
            ActionChains(browser).move_to_element(tpl).perform()
            # ActionChains(browser).context_click(tpl).send_keys('S').perform()

            print(name)
            print(url)
            print(url_qr)
            data = request.urlopen(url).read()
            # data = opener.open(url).read()
            f = open(root_path + "/" + name + ".jpg", "wb")
            f.write(data)
            f.close()

            # data = request.urlopen(url2).read()
            req1 = request.Request(
                url=url_qr,
                headers=headers)
            response = request.urlopen(req1)
            data = response.read()
            f = open(root_path + "/" + name + "_qr.png", "wb")
            f.write(data)
            f.close()

    # < div class ="tpl_item clearfix" >
    #     < img class ="tpl_img" data-value="208" src="http://cdn.xcx.weijuju.com/2018/7/common/default/16080d1c-7ba2-10a1-f65e-fd7a82a2.jpeg" >
    # < div class ="anli_content_box" style="transform: translateX(100%);" >
    # < div class ="qrcode_img_box" >
    # < img class ="qrcode_img" data-value="208" src="/admin/config/getPreviewQrcode.do?page=pages%2Findex%2Ftpl_index&amp;scene=tplid%3D208" > < / div > < p > 扫码体验 < / p > < p class ="demo_tips" > demo预览模式 < / p > < / div > < div class ="tip_div" > < div style="color:#6E6E6E;    margin-bottom:10px;" > 名酒商贸 < / div > < a href="javascript:;" class ="btn btn-primary start acppshopEdit" data-value="208" data-type="custom" > 启用 < / a > < a href="javascript:;" class ="btn btn-primary pubTpl hide" data-id="208" > 发布 < / a > < a href="shopedit.jsp?action=edit&amp;tpl=208" target="_blank" class ="btn btn-primary edit acppshopEdit" data-value="208" data-type="custom" > 编辑 < / a > < / div > < / div >
    #


if __name__ == "__main__":
    # cmd, first_arg = sys.argv
    # if first_arg is None:
    #     sys.exit(-1)
    print(os.getcwd())
    getshopTempleteMap("x", "x")
