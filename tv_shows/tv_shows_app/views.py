from django.shortcuts import render, redirect
from .models import Show

def index(request):
    return redirect('/shows')

def shows(request):
    context = {
        'shows': Show.objects.all()
    }
    return render(request, 'tv_shows_app/index.html', context)

def new(request):
    return render(request, 'tv_shows_app/new.html')

def create(request):
    if request.method == "POST":
        show = Show.objects.create(
            title=request.POST['title'],
            network=request.POST['network'],
            release_date=request.POST['release_date'],
            description=request.POST['description']
        )
        return redirect(f'/shows/{show.id}')
    return redirect('/shows/new')

def show(request, id):
    context = {
        'show': Show.objects.get(id=id)
    }
    return render(request, 'tv_shows_app/show.html', context)

def edit(request, id):
    context = {
        'show': Show.objects.get(id=id)
    }
    return render(request, 'tv_shows_app/edit.html', context)

def update(request, id):
    if request.method == "POST":
        show = Show.objects.get(id=id)
        show.title = request.POST['title']
        show.network = request.POST['network']
        show.release_date = request.POST['release_date']
        show.description = request.POST['description']
        show.save()
        return redirect(f'/shows/{show.id}')
    return redirect(f'/shows/{id}/edit')

def destroy(request, id):
    if request.method == "POST":
        show = Show.objects.get(id=id)
        show.delete()
    return redirect('/shows')
