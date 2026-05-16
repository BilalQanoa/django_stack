from django.shortcuts import render, redirect

# Create your views here.

def index(request):
    return render(request, 'form.html')

def submit(request):
    if request.method == 'POST':
        context = {
            'name': request.POST.get('name'),
            'location': request.POST.get('location'),
            'language': request.POST.get('language'),
            'comment': request.POST.get('comment'),
            'gender': request.POST.get('gender'),
            'terms': request.POST.get('terms')
        }
        return render(request, 'result.html', context)
    else:
        return redirect('index')
    