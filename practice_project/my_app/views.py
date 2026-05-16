from django.shortcuts import render, redirect

def index(request):
    # this route shows the form
    return render(request, "index.html")

def create_user(request):
    # this route processes the form
    name_from_form = request.POST['name']
    email_from_form = request.POST['email']
    request.session['name'] = name_from_form
    request.session['email'] = email_from_form
    return redirect("/success")

def success(request):
    # this is the success route
    context = {
        "name": request.session['name'],
        "email": request.session['email']
    }
    return render(request, "success.html", context)
