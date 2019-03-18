from django.shortcuts import render
from django.http import HttpResponseRedirect, FileResponse
from app.models import ChatData, User
import os
import time
import os.path 
import shutil

CACHE_FILE = "cache.txt"
NUMBER_FILE = "number.txt"
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

def welcome(request):
    return render(request, 'welcome.html')

def index(request):
    return render(request,'index.html')

def submitProblem(request):
    message = request.POST.get('input')
    file = open(CACHE_FILE, 'a')
    file.write(message+'\n')
    file.close()
    print (message)
    return render(request,'add_number.html')

def submitNumber(request):
    message = request.POST.get('number')
    file = open(NUMBER_FILE, 'a')
    file.write(message+'\n')
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
    response['Content-Type']='application/msword' 
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