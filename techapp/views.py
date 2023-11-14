from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def login(request):
    return render(request,'login.html')

def dashboard(request):
    username=request.GET['username']
    return render(request, 'dashboard.html',{'name':username})

def register(request):
    return render(request, 'register.html')