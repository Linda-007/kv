import json

import requests


class TestDetaile:
    def setup(self):
        pass
    # 预约就诊详情
    def test_jiuzhen_info(self):
        url = "http://192.168.10.123:1200/appointment/insured/info"
        data = {
            "cPkId": "",
            "cPlyPartNo": "",
            "cPlyPartStatus": ""
        }
        r_info = requests.get(url,json.dumps(data))
        print(r_info.json)

    #预约就诊列表
    def test_jiuzhen_list(self):
        url = "http://192.168.10.123:1200/appointment/insured/list"
        data = {
            "cInsuredName": "",
            "cPlyNo": "",
            "cPlyPartNo": "",
            "cPlyPartStatus" : "",
            "cPrincipalCertCde": "",
            "cWelfareName": "",
            "order": "",
            "orderBy": "",
            "pageNum": "",
            "pageSize": "",
            "tBirthTm":""
        }
        r_list = requests.get(url,json.dumps(data))
        print(r_list.json)

    #预约就诊详情个人信息修改
    def test_update_info(self):
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
        r_update_list = requests.put(url,json.dumps(data))
        print(r_update_list.json)

    # 跟进任务列表
    def test_genjin_task(self):
        url = "http://192.168.10.123:1200/appointment/task"
        data = {
            "createTime":"",
            "delete":"",
            "hangUp":"",
            "hospital": "",
            "kfNo": "",
            "order": "",
            "orderBy": "",
            "orderId": "",
            "pageNum": "",
            "pageSize": "",
            "patientIdCard": "",
            "patientName": "",
            "status": "",
            "visitTime": "",
        }
        r_task = requests.get(url, json.dumps(data))
        print(r_task.json)

    # 跟进任务获取客服
    def test_kefu(self):
        url = "http://192.168.10.123:1200/appointment/kefu"
        data = {
            "kfNo" : "",
        }
        r_kefu = requests.get(url,json.dumps(data))
        print(r_kefu.json)

    #历史工单列表
    def test_order_history(self):
        url = "http://192.168.10.123:1200/appointment/history"
        data = {
            "createTime": "",
            "delete": "",
            "hangUp": "",
            "hospital": "",
            "kfNo": "",
            "order": "",
            "orderBy": "",
            "orderId": "",
            "pageNum": "",
            "pageSize":"",
            "patientIdCard": "",
            "patientName": "",
            "status": "",
            "visitTime": "",
        }
        r_history = requests.get(url, json.dumps(data))
        print(r_history.json)

    # 历史工单详情
    def test_history_order_info(self):
        url = "http://192.168.10.123:1200/appointment/history/get"
        data = {
            "orderId": "",
        }
        r_history_info = requests.get(url, json.dumps(data))
        print(r_history_info.json)

    # 签约医院列表
    def test_hospital_list(self):
        url = "http://192.168.10.123:1200/appointment/hospital/list"
        data = {
            "CHospNo":"",
            "CHospName": "",
            "CCityName": "",
            "CHospitalNature": "",
            "CCooperationStatus": "",
            "CHospAddr": "",
            "CHospTypName": "",
            "CIsOpeningAllDay": "",
        }
        r_hospital_list = requests.post(url,json.dumps(data))
        print(r_hospital_list.json)

    # 签约医院详情
    def test_hospital_info(self):
        url = "http://192.168.10.123:1200/appointment/hospital/info"
        data = {
            "CHospNo":"",
        }
        r_hospital_info = requests.post(url,json.dumps(data))
        print(r_hospital_info.json)

    #联想查询城市
    def test_getcity(self):
        url = "http://192.168.10.123:1200/appointment/hospital/getcity"
        data = {
            "city":"",
        }
        r_getcity = requests.get(url,json.dumps(data))
        print(r_getcity.json)

    #导出列表
    def test_export_list(self):
        url = "http://192.168.10.123:1200/appointment/hospita/lexport"
        data = {
            "CHospNo":"",
            "CHospName": "",
            "CCityName": "",
            "CHospitalNature": "",
            "CCooperationStatus": "",
            "CHospAddr": "",
            "CHospTypName": "",
            "CIsOpeningAllDay": "",

        }
        r_export_list = requests.post(url,json.dump(data))
        print(r_export_list.json)

    # 字典匹配
    def test_pipei_dict(self):
        url = "http://192.168.10.123:1200/appointment/dict"
        data = {
            "cCde": "",
            "cCnm": "",
            "cParent":"",
            "pageNum": "",
            "pageSize": "",
        }
        r_dict = requests.get(url,json.dumps(data))
        print(r_dict.json)