import json
# -*- coding:utf-8 -*-
import requests


class TestLogin:
    def setup(self):
        pass
    # 传入正确的密码账号，登录成功
    def test_right_login(self):
        url = "http://192.168.10.123:1200/auth/user/login"
        data = {
            "username":"0001",
            "password":"123456"
        }
        r_login = requests.post(url,json.dumps(data))
        print(r_login.json)


    #传入错误账号，登录失败
    def test_error_login(self):
        url = "http://192.168.10.123:1200/auth/user/login"
        data = {
            "username": "01",
            "password": "123456"
        }
        r_login = requests.post(url, json.dumps(data))
        print(r_login.json)

    #传入错误密码，登录失败
    def test_error_password(self):
        url = "http://192.168.10.123:1200/auth/user/login"
        data = {
            "username": "0001",
            "password": "1234567"
        }
        r_login = requests.post(url, json.dumps(data))
        print(r_login.json)

    #用户名为空，登录失败
    def test_null_username(self):
        url = "http://192.168.10.123:1200/auth/user/login"
        data = {
            "username": "",
            "password": "123456"
        }
        r_login = requests.post(url, json.dumps(data))
        print(r_login.json)

    # 密码为空，登录失败
    def test_null_password(self):
        url = "http://192.168.10.123:1200/auth/user/login"
        data = {
            "username": "0001",
            "password": ""
        }
        r_login = requests.post(url, json.dumps(data))
        print(r_login.json)

    #不传入用户名，登录失败
    def test_zero_username(self):
        url = "http://192.168.10.123:1200/auth/user/login"
        data = {

            "password": "123456"
        }
        r_login = requests.post(url, json.dumps(data))
        print(r_login.json)

    # 不传入密码，登录失败
    def test_zero_password(self):
        url = "http://192.168.10.123:1200/auth/user/login"
        data = {

             "username": "0001",
        }
        r_login = requests.post(url, json.dumps(data))
        print(r_login.json)
