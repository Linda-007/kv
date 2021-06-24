import json

import requests


def test_null_data():
    url = "http://192.168.10.123:1200/appointment/insured/info"
    data = {
        "cPkId": "",
        "cPhone1": "",
        "cPhone2": "",
        "cEmail": "",
        "cAddr": "",
        "cIssueStatusOfMembershipCard": "",
        "note1": "",
        "Note2": "",
        "Note3": "",
    }
    r_update_list = requests.put(url, json.dumps(data))
    print(r_update_list.json)

def test_null_beibaoxian():
    url = "http://192.168.10.123:1200/appointment/insured/info"
    data = {
        "cPkId": "",
        "cPhone1": "135134354",
        "cPhone2": "175654511",
        "cEmail": "4123412@qq.com",
        "cAddr": "成都市金牛区",
        "cIssueStatusOfMembershipCard": "打印中",
        "note1": "12",
        "Note2": "",
        "Note3": "",
    }
    r_update_list = requests.put(url, json.dumps(data))
    print(r_update_list.json)

def test_nostr_beibaoxian():
    url = "http://192.168.10.123:1200/appointment/insured/info"
    data = {
        "cPkId": 4028886579abbc980179aca6e7a0028b,
        "cPhone1": "135134354",
        "cPhone2": "175654511",
        "cEmail": "4123412@qq.com",
        "cAddr": "成都市金牛区",
        "cIssueStatusOfMembershipCard": "打印中",
        "note1": "12",
        "Note2": "",
        "Note3": "",
    }
    r_update_list = requests.put(url, json.dumps(data))
    print(r_update_list.json)

def test_ture_beibaoxian():
    url = "http://192.168.10.123:1200/appointment/insured/info"
    data = {
        "cPkId": "4028886579abbc980179aca6e7a0028b",
        "cPhone1": "135134354",
        "cPhone2": "175654511",
        "cEmail": "4123412@qq.com",
        "cAddr": "成都市金牛区",
        "cIssueStatusOfMembershipCard": "打印中",
        "note1": "12",
        "Note2": "",
        "Note3": "",
    }
    r_update_list = requests.put(url, json.dumps(data))
    print(r_update_list.json)

def test_false_beibaoxian():
    url = "http://192.168.10.123:1200/appointment/insured/info"
    data = {
        "cPkId": "手机号4028886579abbc980179aca6e7a0028b",
        "cPhone1": "135134354",
        "cPhone2": "175654511",
        "cEmail": "4123412@qq.com",
        "cAddr": "成都市金牛区",
        "cIssueStatusOfMembershipCard": "打印中",
        "note1": "12",
        "Note2": "",
        "Note3": "",
    }
    r_update_list = requests.put(url, json.dumps(data))
    print(r_update_list.json)