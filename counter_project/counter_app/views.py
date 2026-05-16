from django.shortcuts import render, redirect

# index view to display the counter value and increment it on each page load
def index(request):
    if 'counter' not in request.session:
        request.session['counter'] = 1
    else:
        request.session['counter'] += 1
    return render(request, 'index.html')


def destroy(request):
    request.session.clear()
    return redirect('index')

def add_two(request):
    if 'counter' not in request.session:
        request.session['counter'] = 2
    else:
        request.session['counter'] += 1
    return redirect('index')

def add_specific(request):
    amount = int(request.POST.get('amount'))
    if 'counter' not in request.session:
        request.session['counter'] = amount
    else:
        request.session['counter'] += amount - 1
    return redirect('index')