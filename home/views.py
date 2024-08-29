from django.shortcuts import render

from django.http import HttpResponse

def home(request):
    peoples = [
        {"name": "Satyam Singh", "age":24},
        {"name": "Adarsh", "age":44},
        {"name": "Bhawesh", "age":84},
        {"name": "Vinayak", "age":24}
    ]
    return render(request, "index.html", context={'peoples': peoples})

def sucess(request):
    return HttpResponse("<H1>Hey! This is the Sucess Page</h1>")
# Create your views here.
