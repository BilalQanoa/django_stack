from django.shortcuts import render, redirect, get_object_or_404
from .models import Book, Author

def books_index(request):
    if request.method == "POST":
        title = request.POST.get("title")
        desc = request.POST.get("desc")
        Book.objects.create(title=title, desc=desc)
        return redirect("/")

    context = {
        "books": Book.objects.all()
    }
    return render(request, "books_authors_app/books.html", context)

def book_detail(request, book_id):
    book = get_object_or_404(Book, id=book_id)
    if request.method == "POST":
        author_id = request.POST.get("author_id")
        if author_id:
            author = get_object_or_404(Author, id=author_id)
            book.authors.add(author)
        return redirect("book_detail", book_id=book_id)
        
    context = {
        "book": book,
        "authors": book.authors.all(),
        "available_authors": Author.objects.exclude(books=book)
    }
    return render(request, "books_authors_app/book_detail.html", context)

def authors_index(request):
    if request.method == "POST":
        first_name = request.POST.get("first_name")
        last_name = request.POST.get("last_name")
        notes = request.POST.get("notes")
        Author.objects.create(first_name=first_name, last_name=last_name, notes=notes)
        return redirect("/authors")

    context = {
        "authors": Author.objects.all()
    }
    return render(request, "books_authors_app/authors.html", context)

def author_detail(request, author_id):
    author = get_object_or_404(Author, id=author_id)
    if request.method == "POST":
        book_id = request.POST.get("book_id")
        if book_id:
            book = get_object_or_404(Book, id=book_id)
            author.books.add(book)
        return redirect("author_detail", author_id=author_id)

    context = {
        "author": author,
        "books": author.books.all(),
        "available_books": Book.objects.exclude(authors=author)
    }
    return render(request, "books_authors_app/author_detail.html", context)
