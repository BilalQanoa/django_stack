from django.shortcuts import render, redirect
from django.contrib import messages
from django.utils import timezone
from datetime import timedelta
from login_app.models import User
from .models import Message, Comment

def wall(request):
    if 'user_id' not in request.session:
        return redirect('/') # Redirect to login page
    
    context = {
        'user': User.objects.get(id=request.session['user_id']),
        'messages': Message.objects.all().order_by('-created_at')
    }
    return render(request, 'wall_app/wall.html', context)

def post_message(request):
    if request.method == 'POST':
        if 'user_id' not in request.session:
            return redirect('/')
        user = User.objects.get(id=request.session['user_id'])
        Message.objects.create(
            user=user,
            message_content=request.POST.get('message_content')
        )
    return redirect('/wall')

def post_comment(request, message_id):
    if request.method == 'POST':
        if 'user_id' not in request.session:
            return redirect('/')
        user = User.objects.get(id=request.session['user_id'])
        message = Message.objects.get(id=message_id)
        Comment.objects.create(
            user=user,
            message=message,
            comment_content=request.POST.get('comment_content')
        )
    return redirect('/wall')

def delete_message(request, message_id):
    if request.method == 'POST':
        if 'user_id' not in request.session:
            return redirect('/')
        
        try:
            message = Message.objects.get(id=message_id)
        except Message.DoesNotExist:
            return redirect('/wall')

        # NINJA BONUS: Validate owner
        if message.user.id != request.session['user_id']:
            messages.error(request, "You are not allowed to delete this message.")
            return redirect('/wall')

        # SENSEI BONUS: Validate 30 minutes
        if timezone.now() - message.created_at > timedelta(minutes=30):
            messages.error(request, "Messages older than 30 minutes cannot be deleted.")
            return redirect('/wall')

        message.delete()
        messages.success(request, "Message deleted successfully.")
    return redirect('/wall')
