# -*- coding: utf-8 -*-

import requests
from requests.packages.urllib3.exceptions import InsecureRequestWarning
requests.packages.urllib3.disable_warnings(InsecureRequestWarning)

http_session = requests.Session()
http_headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.113 Safari/537.36',
    'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
    'x-requested-with': 'XMLHttpRequest'
}


def get(url):
    response = http_session.get(url, headers=http_headers, verify=False)
    return response.text if response.status_code == 200 else None


def post(url, data={}, referer=''):
    if referer is not '':
        http_headers['Referer'] = str(referer)
    response = http_session.post(url, data, headers=http_headers, verify=False)
    return response.text if response.status_code == 200 else None
