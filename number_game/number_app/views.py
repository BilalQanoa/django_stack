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
        user_guess = int(request.POST['guess'])
        request.session['attempts'] += 1
        target = request.session['target_num']

        if user_guess < target:
            request.session['status'] = 'low'
        elif user_guess > target:
            request.session['status'] = 'high'
        else:
            request.session['status'] = 'correct'

        if request.session['attempts'] >= 5 and request.session['status'] != 'correct':
            request.session['status'] = 'lose'
            
        request.session.modified = True
    return redirect('/')

def submit_score(request):
    if request.method == 'POST':
        name = request.POST['name']
        attempts = request.session.get('attempts', 0)
        leaderboard = request.session.get('leaderboard', [])
        leaderboard.append({'name': name, 'attempts': attempts})
        leaderboard.sort(key=lambda x: x['attempts'])
        request.session['leaderboard'] = leaderboard[:10] 
        request.session.modified = True
    return redirect('/leaderboard')

def reset(request):

    request.session['target_num'] = random.randint(1, 100)
    request.session['attempts'] = 0
    request.session['status'] = None
    request.session.modified = True
    return redirect('/')

def leaderboard(request):
    context = {
        'leaderboard': request.session.get('leaderboard', [])
    }
    return render(request, "leaderboard.html", context)