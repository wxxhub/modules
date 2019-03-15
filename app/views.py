from django.shortcuts import render
from django.http import HttpResponseRedirect  
from app.models import ChatData, User
import os

CACHE_FILE = "cache.txt"
NUMBER_FILE = "number.txt"

def welcome(request):
    return render(request, 'welcome.html')

def index(request):
    return render(request,'index.html')

def submitProblem(request):
    problem = request.POST.get('bubble')
    message = request.POST.get('input')
    if problem != None:
        message = problem
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
    return HttpResponseRedirect('https://www.baidu.com/')