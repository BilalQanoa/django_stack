from django.shortcuts import render, redirect
from . import forms
from django.views import generic
from .models import Review

# Create your views here.

# class based view (CBV)
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
    success_url = '/test/lists'
    # template_name= '' # or the default will be : appname/modelname_form.html

class ListsRviews (generic.ListView):
    model = Review
    template_name = 'lists.html'
    context_object_name = 'lists' # defalut = object_list
    queryset = Review.objects.all().order_by('-id')

    # add context in django CBV
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['var'] = Review.objects.all().order_by('-id')
        return context

class Details (generic.DetailView):
    model = Review
    template_name = 'details.html'
    context_object_name = 'review'

class Update (generic.UpdateView):
    model = Review
    fields = '__all__'
    success_url = '/test/lists'

class Delete (generic.DeleteView):
    model = Review
    success_url = '/test/lists'
    template_name = 'confirm_delete.html'