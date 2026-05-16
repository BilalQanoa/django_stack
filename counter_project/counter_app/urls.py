from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('destroy/', views.destroy, name='destroy'),
    path('add_two/', views.add_two, name='add_two'),
    path('add_specific/', views.add_specific, name='add_specific')

]