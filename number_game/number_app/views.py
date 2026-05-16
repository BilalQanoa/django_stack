from django.shortcuts import render, redirect

import random

def index(request):
    if 'target_num' not in request.session:
        request.session['target_num'] = random.randint(1, 100)
        request.session['attempts'] = 0
        request.session['status'] = None
    return render(request, "index.html")

def guess(request):
    if request.method == 'POST':
        guess = int(request.POST['guess'])
        request.session['attempts'] += 1
        target_num = request.session['target_num']
        
        if guess < target_num:
            request.session['status'] = 'low'
        elif guess > target_num:
            request.session['status'] = 'high'
        else:
            request.session['status'] = 'correct'
        request.session.modifies = True
    return redirect('/')

def reset(request):
    request.session.clear()
    return redirect('/')