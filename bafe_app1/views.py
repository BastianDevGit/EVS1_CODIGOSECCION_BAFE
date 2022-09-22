from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def display(request):
    return HttpResponse('<h1>Hola mundo vista uno app uno</h1>')

def display2(request):
    return HttpResponse('<h1>Hola mundo vista dos app uno</h1>')
