from django.shortcuts import render, redirect
from . import forms
from django.views import generic
from .models import Review

# Create your views here.

# class based view (VBV)
class Home (generic.TemplateView):
    template_name = 'home.html'

class Form (generic.FormView):
    form_class = forms.TestForm
    template_name = 'form.html'
    success_url = '/test'

    def form_valid(self, form):
        print(form.cleaned_data)
        form.save()
        return super().form_valid(form)
    
class CreatePerson (generic.CreateView):
    model = Review
    fields = '__all__'
    success_url = '/test'