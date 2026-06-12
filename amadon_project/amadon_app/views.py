from django.shortcuts import render, redirect
from django.db.models import Sum
from .models import Product, Order

def index(request):
    context = {
        'products': Product.objects.all()
    }
    return render(request, 'store.html', context)

def buy(request):
    if request.method == 'POST':
        product_id = request.POST.get('product_id')
        quantity_str = request.POST.get('quantity', '1')
        
        try:
            quantity = int(quantity_str)
            product = Product.objects.get(id=product_id)
            total_price = product.price * quantity
            
            # Save the new order
            order = Order.objects.create(
                quantity_ordered=quantity,
                total_price=total_price
            )
            
            # Store the current order id in session to display its cost on checkout page
            request.session['last_order_id'] = order.id
            
            # Track user's total purchases in session
            if 'total_quantity' not in request.session:
                request.session['total_quantity'] = 0
            if 'total_spent' not in request.session:
                request.session['total_spent'] = 0.0
            
            request.session['total_quantity'] += quantity
            request.session['total_spent'] += float(total_price)
            
        except (Product.DoesNotExist, ValueError):
            pass # Handle error gracefully, or just pass to redirect

        return redirect('/amadon/checkout/')
    return redirect('/amadon/')

def checkout(request):
    last_order_id = request.session.get('last_order_id')
    last_order = None
    if last_order_id:
        last_order = Order.objects.filter(id=last_order_id).first()
    
    context = {
        'last_order': last_order,
        'total_quantity': request.session.get('total_quantity', 0),
        # Formatting total spent to ensure it is nicely displayed
        'total_spent': "{:.2f}".format(request.session.get('total_spent', 0.00)),
    }
    return render(request, 'checkout.html', context)
