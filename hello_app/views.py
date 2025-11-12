from django.shortcuts import render, HttpResponse
from .models import *

def main(request):
    
    return render(request, 'main.html')

def index2(request):
    
    return render(request, 'index2.html')

