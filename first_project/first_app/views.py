from django.shortcuts import render, redirect, HttpResponse
from django.http import JsonResponse

# root(request) redirect to the /blogs route
def root(request):
    return redirect('/blogs')

#index(request) should return the string "placeholder to later display a list of all blogs"
def index(request):
    return HttpResponse("placeholder to later display a list of all blogs")

# new(request) should return the string "placeholder to display a new form to create a new blog"
def new(request):
    return HttpResponse("placeholder to display a new form to create a new blog")

# create(request) should redirect to the "/" route
def create(request):
    return redirect('/')

# show(request, number) should accept a number as a parameter and return the string "placeholder to display blog number: {number}"
def show(request, number):
    return HttpResponse(f"placeholder to display blog number: {number}")

# edit(request, number) should accept a number as a parameter and return the string "placeholder to edit blog {number}"
def edit(request, number):
    return HttpResponse(f"placeholder to edit blog {number}")

# destroy(request, number) should accept a number as a parameter and redirect to the "/blogs" route
def destroy(request, number):
    return redirect('/blogs')

# json(request) should return a JsonResponse with title and content keys.
def json(request):
    return JsonResponse(
                    {
                        'name' : 'Bilal Qanoa',
                        'title': 'My First Blog',
                        'content': 'Hello, this is my first blog post!',
                    })