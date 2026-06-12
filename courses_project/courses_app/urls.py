from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('courses/create', views.create, name='create_course'),
    path('courses/destroy/<int:id>', views.destroy, name='destroy_course'),
    path('courses/destroy/<int:id>/delete', views.delete_course, name='delete_course'),
    path('courses/<int:id>/comments', views.comments, name='comments'),
]
