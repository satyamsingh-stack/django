from django.shortcuts import redirect, render
from .models import *
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib import messages  # Correct import for messages

def reciepes(request):
    if request.method == "POST":
        data = request.POST
        name = data.get('name')
        desc = data.get('description')
        image = request.FILES.get('image')
        
        Receipe.objects.create(
            name=name, 
            description=desc, 
            image=image
        )
        # return render('/reciepes/')

    queryset = Receipe.objects.all()
    context = {'reciepes': queryset}

    return render(request, 'reciepes.html', context)

def delete_rec(request, id):
    queryset = Receipe.objects.get(id=id)
    queryset.delete()
    return render(request, 'reciepes.html') 

def update_recipe(request, id):
    queryset = Receipe.objects.get(id=id)
    if request.method == "POST":
        data = request.POST
        name = data.get('name')
        desc = data.get('description')
        image = request.FILES.get('image')
        queryset.description = desc
        queryset.name = name

        # Update the image if a new one is uploaded
        if image:
            queryset.image = image

        # Save the updated recipe
        queryset.save()

        # Redirect to the recipes view
        return render(request, 'reciepes.html')

    # If not a POST request, render the form with current data
    context = {'recipe': queryset}
    return render(request, 'update_recipe.html', context)

def login(request):
    return render(request, 'login.html')

def register(request):
    if request.method == "POST":
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = User.objects.filter(username=username).exists()
        if User.objects.filter(username=username).exists():
            messages.error(request, "Username already exists")  # Show error message if username exists
            return render(request, 'register.html')
        user = User.objects.create(
            first_name=first_name,
            last_name=last_name,
            username=username
        )
        user.set_password(password)
        user.save()

        # Use the correct messages method to show success
        messages.success(request, "Account created successfully")
        return render(request, 'register.html')  # Redirect to login after successful registration

    return render(request, 'register.html')
