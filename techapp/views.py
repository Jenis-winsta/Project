from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def login(request):
    return render(request,'login.html')

def dashboard(request):
    username=request.POST['username']
    return render(request, 'dashboard.html',{'name':username})

def register(request):
    # username=request.POST['username']
    # password=request.POST['password']
    return render(request, 'register.html')