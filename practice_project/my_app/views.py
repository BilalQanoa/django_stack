from django.shortcuts import render, redirect

def index(request):
    # this route shows the form
    return render(request, "index.html")

def create_user(request):
    # this route processes the form
    name_from_form = request.POST['name']
    email_from_form = request.POST['email']
    return redirect("/success")

def success(request):
    # this is the success route
    return render(request, "success.html")
