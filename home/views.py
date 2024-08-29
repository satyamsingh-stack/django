from django.shortcuts import render

from django.http import HttpResponse

def home(request):
    return render(request,"index.html")

def sucess(request):
    return HttpResponse("<H1>Hey! This is the Sucess Page</h1>")
# Create your views here.
