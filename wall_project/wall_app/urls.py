from django.urls import path
from . import views

urlpatterns = [
    path('wall', views.wall, name='wall'),
    path('wall/post_message', views.post_message, name='post_message'),
    path('wall/post_comment/<int:message_id>', views.post_comment, name='post_comment'),
    path('wall/delete_message/<int:message_id>', views.delete_message, name='delete_message'),
]
