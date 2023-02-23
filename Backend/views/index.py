#  负责渲染html文件 将文件结构生成好
from django.shortcuts import render
from django.http import JsonResponse
from django.shortcuts import redirect

def index(request):
    return render(request,'index.html')