import json
# -*- coding:utf-8 -*-
import requests


class TestDetaile:
    def test_all_null(self):
        url = "http://192.168.10.123:1200/appointment/insured/info"
        data = {
            "cPkId": "",
            "cPlyPartNo": "",
            "cPlyPartStatus": ""
        }
        r_info = requests.get(url, json.dumps(data))
        print(r_info.json)

    def test_data_null(self):
        url = "http://192.168.10.123:1200/appointment/insured/info"
        data = {

        }
        r_info = requests.get(url, json.dumps(data))
        print(r_info.json)

    def test_data_null(self):
        url = "http://192.168.10.123:1200/appointment/insured/info"
        data = {

        }
        r_info = requests.get(url, json.dumps(data))
        print(r_info.json)

    def test_all_null(self):
        url = "http://192.168.10.123:1200/appointment/insured/info"
        data = {
            "cPkId": "4028886579abbc980179aca6e7a0028b",
            "cPlyPartNo": "99012744890147902",
            "cPlyPartStatus": "Expired"
        }
        r_info = requests.get(url, json.dumps(data))
        print(r_info.json)

    def test_all_data(self):
        url = "http://192.168.10.123:1200/appointment/insured/info"
        data = {
            "cPkId": "4028886579abbc980179aca6e7a0028b",
            "cPlyPartNo": "99012744890147902",
            "cPlyPartStatus": "Expired"
        }
        r_info = requests.get(url, json.dumps(data))
        print(r_info.json)

    # def test_cn_data(self):
    #     url = "http://192.168.10.123:1200/appointment/insured/info"
    #     data = {
    #         "cPkId": "4028886579abbc980179aca6e7a0028b",
    #         "cPlyPartNo": "ddd",
    #         "cPlyPartStatus": "Expired"
    #     }
    #     r_info = requests.get(url, json.dumps(data))
    #     print(r_info.json)
