from django.urls import path
from . import views

app_name = 'test'
urlpatterns = [
    path('', views.Home.as_view(), name='home'),
    path('form/', views.Form.as_view(), name='form'),
    path('create/', views.CreatePerson.as_view(), name='create')
]
