#  负责渲染html文件 将文件结构生成好
from django.shortcuts import render
from django.http import JsonResponse

def index(request):
    return  JsonResponse({
        'result':'success',
        })