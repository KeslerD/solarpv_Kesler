from django.shortcuts import render
from django.urls import reverse
from django.views.generic.base import RedirectView

def index(request):
    return render(request,'index.html')
    
def registration(request):
    return render(request,'registration.html')
    
def login(request):
    return render(request, 'login.html')

def searchCert(request):
    return render(request,'searchCert.html')

def adminRedirect(request):
    return render(request,'admin.html')