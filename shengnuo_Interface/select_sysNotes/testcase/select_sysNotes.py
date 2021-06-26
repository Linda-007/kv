# -*- coding:utf-8 -*-
import json

import requests


class TestSysNotes:
    def setup(self):
        pass
    # 传入预约就诊工单号、页码、当前页数据量，应查询到对应备注信息
    def test_all_data(self):
        url = "http://192.168.10.123:1200/appointment/sysNotes"
        data = {
            "pageNum":"1",
            "pageSize":"5",
            "workOrderNo":"KF20210611009"
        }
        r_notes = requests.get(url,json.dumps(data))
        print(r_notes.json)
    #只传入预约就诊工单号，应查询到对应备注信息
    def test_only_data(self):
        url = "http://192.168.10.123:1200/appointment/sysNotes"
        data = {

            "workOrderNo":"KF20210611009"
        }
        r_notes = requests.get(url,json.dumps(data))
        print(r_notes.json)
    #传入预约就诊工单号为中文汉字，应查询不到对应备注信息
    def test_cn_workOrderNo(self):
        url = "http://192.168.10.123:1200/appointment/sysNotes"
        data = {
            "pageNum": "1",
            "pageSize": "5",
            "workOrderNo": "哈喽"

        }
        r_notes = requests.get(url,json.dumps(data))
        print(r_notes.json)
    #传入预约就诊页码为汉字+英文，查询不到对应备注信息
    def test_cnen_pageNum(self):
        url = "http://192.168.10.123:1200/appointment/sysNotes"
        data = {
            "pageNum": "all页",
            "pageSize": "5",
            "workOrderNo": "KF20210611009"

        }
        r_notes = requests.get(url,json.dumps(data))
        print(r_notes.json)

    #入预约就诊页码为非int数据，查询不到对应备注信息
    def test_nostr_pageNum(self):
        url = "http://192.168.10.123:1200/appointment/sysNotes"
        data = {
            "pageNum": "1.0",
            "pageSize": "5",
            "workOrderNo": "KF20210611009"

        }
        r_notes = requests.get(url,json.dumps(data))
        print(r_notes.json)

    #传入预约就诊当前页数据量为非int数据，查询不到对应备注信息
    def test_nostr_pageSize(self):
        url = "http://192.168.10.123:1200/appointment/sysNotes"
        data = {
            "pageNum": "1",
            "pageSize": "5.0",
            "workOrderNo": "KF20210611009"

        }
        r_notes = requests.get(url,json.dumps(data))
        print(r_notes.json)
    #传入预约就诊工单号未空值，查询不到数据
    def test_null_workOrderNo(self):
        url = "http://192.168.10.123:1200/appointment/sysNotes"
        data = {
            "pageNum": "1",
            "pageSize": "5",
            "workOrderNo": ""

        }
        r_notes = requests.get(url,json.dumps(data))
        print(r_notes.json)

    #传入页码为空值，应查询不到对应备注信息
    def test_null_pageNum(self):
        url = "http://192.168.10.123:1200/appointment/sysNotes"
        data = {
            "pageNum": "",
            "pageSize": "5",
            "workOrderNo": "KF20210611009"
        }
        r_notes = requests.get(url, json.dumps(data))
        print(r_notes.json)
    #传入页码数据量为空值，应查询不到对应备注信息
    def test_null_pageSize(self):
        url = "http://192.168.10.123:1200/appointment/sysNotes"
        data = {
            "pageNum": "1",
            "pageSize": "",
            "workOrderNo": "KF20210611009"
        }
        r_notes = requests.get(url, json.dumps(data))
        print(r_notes.json)

    #不传预约工单号，查询不到数据
    def test_zero_workOrderNo(self):
        url = "http://192.168.10.123:1200/appointment/sysNotes"
        data = {
            "pageNum": "1",
            "pageSize": "",

        }
        r_notes = requests.get(url, json.dumps(data))
        print(r_notes.json)

    #不传入页码，应查询不到对应备注信息
    def test_zero_pageNum(self):
        url = "http://192.168.10.123:1200/appointment/sysNotes"
        data = {

            "pageSize": "2",
            "workOrderNo": "KF20210611009"
        }
        r_notes = requests.get(url, json.dumps(data))
        print(r_notes.json)

    #不传入页码数据量，应查询不到对应备注信息
    def test_zero_pageSize(self):
        url = "http://192.168.10.123:1200/appointment/sysNotes"
        data = {
            "pageNum": "1",
            "workOrderNo": "KF20210611009"
        }
        r_notes = requests.get(url, json.dumps(data))
        print(r_notes.json)

    #pageNmu<1时，查询失败
    def test_pageNum(self):
        url = "http://192.168.10.123:1200/appointment/sysNotes"
        data = {
            "pageNum": "0",
            "pageSize": "2",
            "workOrderNo": "KF20210611009"
        }
        r_notes = requests.get(url, json.dumps(data))
        print(r_notes.json)

    #pageSize<0,查询失败
    def test_pageSize(self):
        url = "http://192.168.10.123:1200/appointment/sysNotes"
        data = {
            "pageNum": "0",
            "pageSize": "-2",
            "workOrderNo": "KF20210611009"
        }
        r_notes = requests.get(url, json.dumps(data))
        print(r_notes.json)
