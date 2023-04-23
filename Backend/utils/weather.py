#!/usr/bin/python
# -*- coding: utf-8 -*-
import httplib2
from urllib.parse import urlencode #python3

def weather(ip):
    params = urlencode({'ip':ip,'type':'1','callback':'find','style':3})
    url = 'https://api.ip138.com/weather/?'+params
    headers = {"token":"80d6884a7dd1bca9f9b2c7e275cfac37"}
    http = httplib2.Http()
    response, content = http.request(url,'GET',headers=headers)
    res = content.decode("utf-8")
    res = res[5: len(res) - 1]
    return res