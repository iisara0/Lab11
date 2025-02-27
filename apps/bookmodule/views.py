from django.shortcuts import render

def index(request):
    return render(request, 'bookmodule/index.html')

def list_books(request):
    # Logic to list books
    return render(request, 'bookmodule/list_books.html')

def about_us(request):
    return render(request, 'bookmodule/aboutus.html')

def one_book(request, bookId):
    return render(request, 'bookmodule/one_book.html')
