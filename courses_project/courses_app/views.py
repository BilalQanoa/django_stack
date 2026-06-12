from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Course, Description, Comment

def index(request):
    context = {
        'courses': Course.objects.all().order_by('-created_at')
    }
    return render(request, 'index.html', context)

def create(request):
    if request.method == "POST":
        errors = Course.objects.basic_validator(request.POST)
        if len(errors) > 0:
            for key, value in errors.items():
                messages.error(request, value)
            return redirect('/')
        else:
            new_course = Course.objects.create(name=request.POST['name'])
            Description.objects.create(content=request.POST['desc'], course=new_course)
            messages.success(request, "Course successfully created!")
            return redirect('/')
    return redirect('/')

def destroy(request, id):
    context = {
        'course': Course.objects.get(id=id)
    }
    return render(request, 'destroy.html', context)

def delete_course(request, id):
    if request.method == "POST":
        course = Course.objects.get(id=id)
        course.delete()
        messages.success(request, "Course successfully deleted!")
    return redirect('/')

def comments(request, id):
    course = Course.objects.get(id=id)
    if request.method == "POST":
        if len(request.POST.get('content', '')) > 0:
            Comment.objects.create(content=request.POST['content'], course=course)
            return redirect(f'/courses/{id}/comments')
        else:
            messages.error(request, "Comment cannot be empty.")
            return redirect(f'/courses/{id}/comments')
    
    context = {
        'course': course,
        'course_comments': course.comments.all().order_by('-created_at')
    }
    return render(request, 'comments.html', context)
