from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    name='jenis'
    return render(request,'index.html',{'name':name})

def dashboard(request):
    username=request.GET['username']
    return render(request, 'dashboard.html',{'name':username})