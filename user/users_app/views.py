from django.shortcuts import render, redirect
from .models import User

# Create your views here.

def index (request):
    context = {
        'users' : User.objects.all()
    }
    return render (request, 'index.html', context)


def create (request):
    first_name = request.POST.get('first_name')
    last_name = request.POST.get('last_name')
    email = request.POST.get('email')
    age = request.POST.get('age')

    User.objects.create(first_name=first_name, last_name=last_name, email=email, age=age)
    return redirect('/')