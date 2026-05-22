from django.urls import path
from . import views

app_name = 'test'
urlpatterns = [
    path('', views.Home.as_view(), name='home'),
    path('form/', views.Form.as_view(), name='form'),
    path('create/', views.CreatePerson.as_view(), name='create'),
    path('lists/', views.ListsRviews.as_view(), name='lists'),
    path('details/<int:pk>', views.Details.as_view(), name='details'),
    path('update/<int:pk>', views.Update.as_view(), name='update'),
    path('delete/<int:pk>', views.Delete.as_view(), name='delete'),
]
