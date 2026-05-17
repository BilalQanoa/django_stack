from django.shortcuts import render, redirect, HttpResponse

def index(request):
    return HttpResponse("placeholder to display all the blogs.")

def new(request):
    return HttpResponse("placeholder for users to add a new blog.")

def create(request):
    return redirect('/blogs')

def show(request, number):
    return HttpResponse(f"placeholder to display blog number: {number}")

def edit(request, number):
    return HttpResponse(f"placeholder to edit blog number: {number}")

def destroy(request, number):
    return redirect('/blogs')
