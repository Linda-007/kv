import json
# -*- coding:utf-8 -*-
import requests
class TestUpdatepassword:
    def setup(self):
        pass
    #传入正确token的情况
    # 传入账号密码和token，修改密码成功
    def test_all_data(self):
        url = "http://192.168.10.123:1200/auth/user/update"
        data = {

        "username":"0001",
        "password":"123456",

        }
        r_list = requests.put(url, data=data)
        #获取token
        return (r_list.json()["data"]["token"])
       # print(r_list.json)

    #只传入账号和Token，修改密码失败
    def test_zero_password(self):
        url = "http://192.168.10.123:1200/auth/user/update"
        data = {

        "username":"0001",
        "token":""

        }
        r_update = requests.post(url,json.dumps(data))

        print(r_update.json)

    #只传入token和密码，修改密码失败
    def test_zero_username(self):
        url = "http://192.168.10.123:1200/auth/user/update"
        data = {

        "password":"123456",
        "token":"",

        }
        r_update = requests.post(url,json.dumps(data))

        print(r_update.json)

    #传入错误账号，正确密码和token，修改失败
    def test_error_username(self):
        url = "http://192.168.10.123:1200/auth/user/update"
        data = {
        "username":"0a",
        "password":"123456",
        "token":"",

        }
        r_update = requests.post(url,json.dumps(data))

        print(r_update.json)

    #传入错误密码，正确账号和token，修改失败
    def test_error_password(self):
        url = "http://192.168.10.123:1200/auth/user/update"
        data = {
        "username":"0001",
        "password":"1234",
        "token":"",

        }
        r_update = requests.post(url,json.dumps(data))

        print(r_update.json)

    #传入空值账号，正确密码和token，修改失败
    def test_null_username(self):
        url = "http://192.168.10.123:1200/auth/user/update"
        data = {
        "username":"",
        "password":"1234",
        "token":"",

        }
        r_update = requests.post(url,json.dumps(data))

        print(r_update.json)

    #传入空值密码，正确账号和token，修改失败
    def test_null_password(self):
        url = "http://192.168.10.123:1200/auth/user/update"
        data = {
        "username":"0001",
        "password":"",
        "token":"",

        }
        r_update = requests.post(url,json.dumps(data))

        print(r_update.json)

    #不传入账号，正确密码和token，修改失败
    def test_zero_username(self):
        url = "http://192.168.10.123:1200/auth/user/update"
        data = {

        "password":"123456",
        "token":"",

        }
        r_update = requests.post(url,json.dumps(data))

        print(r_update.json)

    #不传入密码，正确账号和token，修改失败
    def test_zero_password(self):
        url = "http://192.168.10.123:1200/auth/user/update"
        data = {

        "username":"0001",
        "token":"",

        }
        r_update = requests.post(url,json.dumps(data))

        print(r_update.json)
    # 传入错误token的情况
    #不传入token，正确密码和账号，修改失败
    def test_zero_token(self):
        url = "http://192.168.10.123:1200/auth/user/update"
        data = {

        "username":"0001",
        "password":"123456",

        }
        r_update = requests.post(url,json.dumps(data))

        print(r_update.json)

    #传入错误token，正确密码和账号，修改失败
    def test_error_token(self):
        url = "http://192.168.10.123:1200/auth/user/update"
        data = {

        "username":"0001",
        "password":"123456",
        "token": "%kkk",

        }
        r_update = requests.post(url,json.dumps(data))

        print(r_update.json)
