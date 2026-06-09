from django.urls import path
from . import views

urlpatterns = [
    path('', views.books_index, name='books_index'),
    path('books/<int:book_id>', views.book_detail, name='book_detail'),
    path('authors', views.authors_index, name='authors_index'),
    path('authors/<int:author_id>', views.author_detail, name='author_detail'),
]
