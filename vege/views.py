from django.shortcuts import redirect, render
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

def update_recipe(request,id):
    queryset = Receipe.objects.get(id=id)
    if request.method == "POST":
        data = request.POST
        name = data.get('name')
        desc = data.get('description')
        image= request.FILES.get('image')
        queryset.description = desc
        queryset.name = name

        # Update the image if a new one is uploaded
        if image:
            queryset.image = image

        # Save the updated recipe
        queryset.save()

        # Redirect to the recipes view
        return render(request, 'reciepes.html')   # Assuming your URL pattern name is 'recipes'

    # If not a POST request, render the form with current data
    context = {'recipe': queryset}
    return render(request, 'update_recipe.html', context)