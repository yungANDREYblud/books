from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return HttpResponse("<h4>Проверка работы</4>")

def about(request):
    return HttpResponse("<h4>Проверка</4>")
