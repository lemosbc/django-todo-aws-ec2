from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def taskList(response):
    return HttpResponse('To Do List')
