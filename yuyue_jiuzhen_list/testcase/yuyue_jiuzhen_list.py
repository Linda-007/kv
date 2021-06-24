import json

import requests


def test_null_data():
    url = "http://192.168.10.123:1200/appointment/insured/list"
    data = {
        "cInsuredName": "",
        "cPlyNo": "",
        "cPlyPartNo": "",
        "cPlyPartStatus": "",
        "cPrincipalCertCde": "",
        "cWelfareName": "",
        "order": "",
        "orderBy": "",
        "pageNum": "",
        "pageSize": "",
        "tBirthTm": ""
    }
    r_list = requests.get(url, json.dumps(data))
    print(r_list.json)

def test_one_data():
    url = "http://192.168.10.123:1200/appointment/insured/list"
    data = {

        "cPlyNo": "000100201",
    }
    r_list = requests.get(url, json.dumps(data))
    print(r_list.json)

def test_cn_data():
    url = "http://192.168.10.123:1200/appointment/insured/list"
    data = {

        "cPlyNo": "保单号",

    }
    r_list = requests.get(url, json.dumps(data))
    print(r_list.json)

def test_zero_data():
    url = "http://192.168.10.123:1200/appointment/insured/list"
    data = {

    }
    r_list = requests.get(url, json.dumps(data))
    print(r_list.json)