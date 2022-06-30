"""in this module we are going to define our homepage"""
from django.shortcuts import render


def home(request):
    return render(request,'home.html')