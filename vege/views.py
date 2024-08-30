from django.shortcuts import render
from .models import *
from django.http import HttpResponse

def reciepes(request):
    if request.method == "POST":
        data = request.POST
        name = data.get('name')
        desc = data.get('description')
        image= request.FILES.get('image')
        
        Receipe.objects.create(
            name=name, 
            description=desc, 
            image=image
        )
        # return render('/reciepes/')

    queryset = Receipe.objects.all()
    context = {'reciepes':queryset}

    return render(request, 'reciepes.html', context)

def delete_rec(request,id):
    queryset = Receipe.objects.get(id=id)
    queryset.delete()
    return render(request, 'reciepes.html') 