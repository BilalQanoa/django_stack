from django.shortcuts import redirect, render

# Create your views here.

def index(request):
    if 'gold' not in request.session:
        request.session['gold'] = 0
        request.session['activities'] = []
    return render(request, 'index.html')

def process_money(request):

    if value := request.POST.get('building'):
        import random
        gold_earned = 0
        if value == 'farm':
            gold_earned = random.randint(10, 20)
        elif value == 'cave':
            gold_earned = random.randint(5, 10)
        elif value == 'house':
            gold_earned = random.randint(2, 5)
        elif value == 'casino':
            gold_earned = random.randint(-50, 50)

        request.session['gold'] += gold_earned
        if gold_earned >= 0:
            request.session['activities'].append({
                'message': f"Earned {gold_earned} gold from the {value}!",
                'color': 'green'
            })
        else:
            request.session['activities'].append({
                'message': f"Entered a casino and lost {-gold_earned} gold... Ouch.",
                'color': 'red'
            })
    return redirect('/')

def reset(request):
    request.session.clear()
    return redirect('/')

