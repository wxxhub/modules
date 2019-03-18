#coding=utf-8
from django.shortcuts import render
from django.http import HttpResponseRedirect, FileResponse
from app.models import ChatData, User
import os
import time
import os.path 
import shutil

CACHE_FILE = "cache.txt"
# CACHE_FILE = "number.txt"
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

def welcome(request):
    return render(request, 'welcome.html')

def index(request):
    return render(request,'index.html')

def welcome1(request):
    return render(request, 'welcome1.html')

def index1(request):
    return render(request,'index1.html')

def welcome2(request):
    return render(request, 'welcome2.html')

def index2(request):
    return render(request,'index2.html')

def welcome3(request):
    return render(request, 'welcome3.html')

def index3(request):
    return render(request,'index3.html')

def submitProblem(request):
    message = request.POST.get('input')
    # file = open(CACHE_FILE, 'a')
    # file.write(message+'\n')
    # file.close()
    # print (message)
    return render(request,'add_number.html', {'data':message})

def submitNumber(request):
    number = request.POST.get('number')
    message = "["+ number + ":" + request.POST.get('message') + "]"
    file = open(CACHE_FILE, 'a')
    file.write(message+"\n")
    # file.write()
    file.close()
    return HttpResponseRedirect('https://www.wjx.cn/jq/35975635.aspx')

def download(request):
    return render(request, 'download.html')

def responseFile(request):
    file_name = request.POST.get('download')
    if not os.path.exists(file_name):
        return render(request, 'no_data.html')
    file = open(BASE_DIR+'/'+file_name,'rb')
    response =FileResponse(file) 
    response['Content-Type']='text/plain' 
    response['Content-Disposition']='attachment;filename='+file_name 
    return response

def deleteFile(request):
    file_name = request.POST.get('download')
    new_name = file_name+time.strftime("%Y-%m-%d %H:%M:%S",time.localtime(time.time()))
    shutil.copy(file_name, new_name)
    os.remove(file_name)
    return render(request, 'delete_data.html')

def test(request):
    return render(request, 'test.html')