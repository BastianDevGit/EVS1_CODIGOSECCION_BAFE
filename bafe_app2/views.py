from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def vista1(request):
    return HttpResponse('<h1>Hola mundo vista 1 app 2</h1>')

def vista2(request):
    return HttpResponse('<h1>Hola mundo vista 2 app 2</h1>')

