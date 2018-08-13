import http.cookiejar
from urllib import request
from urllib import parse

import os

if __name__ == '__main__':
    # 登陆地址
    login_url = 'http://new.weijuju.com/login'

    # # User-Agent信息
    # user_agent = r'Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/27.0.1453.94 ' \
    #              r'Safari/537.36 '
    #
    # # Headers信息
    # head = {'User-Agent': user_agent, 'Connection': 'keep-alive'}

    # head['Host'] = 'new.weijuju.com'
    # head['Origin'] = 'http://new.weijuju.com'
    # head['Referer'] = 'http://new.weijuju.com/login.jsp'
    # head['X-Requested-With'] = 'XMLHttpRequest'

    # 登陆Form_Data信息 TODO : 填写自己的名字
    login_data = {'username': '', 'password': ''}

    logingpostdata = parse.urlencode(login_data).encode('utf-8')

    # 保存 cookie 用
    cookie = http.cookiejar.CookieJar()

    # cookie handle
    handler = request.HTTPCookieProcessor(cookie)

    # opener
    opener = request.build_opener(handler)

    opener.open("http://new.weijuju.com/login.jsp")

    for item in cookie:
        print(item.name)
        print(item.value)

    # response = opener.open(fullurl='http://new.weijuju.com/login', data=logingpostdata, headers=head)
    # print(response.read())
    #创建 Request
    # res = request.urlopen(login_url, logingpostdata)
    # print(res.read().decode('utf-8'))
    req1 = request.Request(url=login_url, data=logingpostdata)
    response = opener.open(req1)
    print(response.read().decode('utf-8'))
    for item in cookie:
        print(item.name)
        print(item.value)

    data = opener.open("http://new.weijuju.com/admin/config/getPreviewQrcode.do?page=pages%2Findex%2Ftpl_index&scene=tplid%3D208").read()
    f = open(os.getcwd() + "/qr.png", "wb")
    f.write(data)
    f.close()
