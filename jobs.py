# -*- encoding: utf-8 -*-
"""
@Author: Aloha
@Time: 2024/10/14 22:45
@ProjectName: brandnew
@FileName: jobs.py
@Software: PyCharm
"""
import json
import execjs
import requests


class BossSearch(object):
    def __init__(self):
        self.url = 'https://www.zhipin.com/wapi/zpgeek/search/joblist.json'
        self.cookies = {
        }
        self.headers = {
        }

    def get_data(self):
        response = requests.get(self.url, cookies=self.cookies, headers=self.headers)
        resp = json.loads(response.text)['zpData']
        filename = resp['name']
        seed = resp['seed']
        ts = resp['ts']
        return {
            'filename': filename,
            'seed': seed,
            'ts': str(ts)
        }

    def js_code(self, filename):
        url = f'https://www.zhipin.com/web/common/security-js/{filename}.js'
        cookies = {
        }
        headers = {
        }
        response = requests.get(url, cookies=cookies, headers=headers)
        with open('./zp_token.js', 'r', encoding='utf-8')as f:
            js_file = f.read()
            js_file = js_file.replace("'js_code'", response.text)
            with open('./lol.js', 'w', encoding='utf-8')as f:
                f.write(js_file)

    def job_list(self):
        data = self.get_data()
        self.js_code(data['filename'])
        zp_token = execjs.compile(open('lol.js', 'r', encoding='utf-8').read()).call('zp_token', data['seed'], data['ts'])
        url = 'https://www.zhipin.com/wapi/zpgeek/search/joblist.json'
        cookies = {
            '__zp_stoken__': zp_token,
        }
        headers = {
        }
        params = {
            'scene': '1',
            'query': '数据采集工程师',
            'city': '101280100',
            'experience': '',
            'payType': '',
            'partTime': '',
            'degree': '',
            'industry': '',
            'scale': '',
            'stage': '',
            'position': '',
            'jobType': '',
            'salary': '',
            'multiBusinessDistrict': '',
            'multiSubway': '',
            'page': '5',
            'pageSize': '30',
        }
        response = requests.get(url, params=params, cookies=cookies, headers=headers)
        print(response.text)


if __name__ == '__main__':
    BossSearch().job_list()
