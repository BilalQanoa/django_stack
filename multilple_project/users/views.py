from django.shortcuts import redirect, render, HttpResponse

def index(request):
    return redirect('blogs:index')

def users(request):
    return HttpResponse("placeholder to display all the list of users later.")

def register(request):
    return HttpResponse("placeholder for users to create a new user record.")

def login(request):
    return HttpResponse("placeholder for users to log in.")

def new(request):
    return redirect('/register')

