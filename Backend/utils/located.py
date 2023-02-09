#!/usr/bin/python
# -*- coding: utf-8 -*-
import httplib2
from urllib.parse import urlencode #python3
#from urllib import urlencode #python2
import json
def located(ip):
    try:
        params = urlencode({'ip':ip,'datatype':'jsonp','callback':'find'})
        url = 'https://api.ip138.com/ip/?'+params
        headers = {"token":"c8d82bade82c97954956164c53d4d996"}#token为示例
        http = httplib2.Http()
        response, content = http.request(url,'GET',headers=headers)
        res = content.decode("utf-8")
        res = json.loads(res[5: len(res) - 1])
        return res['data'][1] + res['data'][2]
    except:
        return '中国'
