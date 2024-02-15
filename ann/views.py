from django.shortcuts import render
from django.http import HttpResponse
from django.urls import path

# Create your views here.
def home(request):
    return render(request,'ann/index.html')

def donate(request):
    return render(request, 'ann/donate.html')