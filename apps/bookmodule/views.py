from django.shortcuts import render, redirect, get_object_or_404 , HttpResponse
from django.db.models import Q, Count, Sum, Avg, Max, Min
from .models import Book, Address, Department, Course, Students, Students2
from .forms import BookForm, StudentForm, Student2Form
from django.contrib.auth.decorators import login_required



def student_list(request):
    students = Students.objects.all()
    return render(request, 'bookmodule/lab11/student_list.html', {'students': students})

def student_create(request):
    if request.method == 'POST':
        form = StudentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('student_list')
    else:
        form = StudentForm()
    return render(request, 'bookmodule/lab11/student_form.html', {'form': form})

def student_update(request, pk):
    student = get_object_or_404(Students, pk=pk)
    if request.method == 'POST':
        form = StudentForm(request.POST, instance=student)
        if form.is_valid():
            form.save()
            return redirect('student_list')
    else:
        form = StudentForm(instance=student)
    return render(request, 'bookmodule/lab11/student_form.html', {'form': form})

def student_delete(request, pk):
    student = get_object_or_404(Students, pk=pk)
    if request.method == 'POST':
        student.delete()
        return redirect('student_list')
    return render(request, 'bookmodule/lab11/student_confirm_delete.html', {'student': student})

def student2_list(request):
    students = Students2.objects.all()
    return render(request, 'bookmodule/lab11/student2_list.html', {'students': students})

def student2_create(request):
    if request.method == 'POST':
        form = Student2Form(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('student2_list')
    else:
        form = Student2Form()
    return render(request, 'bookmodule/lab11/student2_form.html', {'form': form})

def student2_update(request, pk):
    student = get_object_or_404(Students2, pk=pk)
    if request.method == 'POST':
        form = Student2Form(request.POST, request.FILES, instance=student)
        if form.is_valid():
            form.save()
            return redirect('student2_list')
    else:
        form = Student2Form(instance=student)
    return render(request, 'bookmodule/lab11/student2_form.html', {'form': form})

def student2_delete(request, pk):
    student = get_object_or_404(Students2, pk=pk)
    if request.method == 'POST':
        student.delete()
        return redirect('student2_list')
    return render(request, 'bookmodule/lab11/student2_confirm_delete.html', {'student': student})

# ----------------------------
# Book Views
@login_required(login_url='/users/login')
def list_books(request):
    books = Book.objects.all()
    return render(request, 'bookmodule/lab9_part1/list_books.html', {'books': books})

@login_required(login_url='/users/login')
def addbook(request):
    if request.method == 'POST':
        Book.objects.create(
            title=request.POST['title'],
            author=request.POST['author'],
            price=float(request.POST['price']),
            edition=int(request.POST['edition'])
        )
        return redirect('list_books')
    return render(request, 'bookmodule/lab9_part1/addbook.html')

@login_required
def editbook(request, id):
    book = get_object_or_404(Book, id=id)
    if request.method == 'POST':
        book.title = request.POST['title']
        book.author = request.POST['author']
        book.price = float(request.POST['price'])
        book.edition = int(request.POST['edition'])
        book.save()
        return redirect('list_books')
    return render(request, 'bookmodule/lab9_part1/editbook.html', {'book': book})

def deletebook(request, id):
    book = get_object_or_404(Book, id=id)
    if request.method == 'POST':
        book.delete()
        return redirect('list_books')
    return render(request, 'bookmodule/lab9_part1/deletebook_confirm.html', {'book': book})

def addbook_form(request):
    if request.method == 'POST':
        form = BookForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('list_books_form')
    else:
        form = BookForm()
    return render(request, 'bookmodule/lab9_part2/addbook_form.html', {'form': form, 'action': 'Add'})

def editbook_form(request, id):
    book = get_object_or_404(Book, id=id)
    if request.method == 'POST':
        form = BookForm(request.POST, instance=book)
        if form.is_valid():
            form.save()
            return redirect('list_books_form')
    else:
        form = BookForm(instance=book)
    return render(request, 'bookmodule/lab9_part2/editbook_form.html', {'form': form, 'action': 'Edit'})

def deletebook_form(request, id):
    book = get_object_or_404(Book, id=id)
    if request.method == 'POST':
        book.delete()
        return redirect('list_books_form')
    return render(request, 'bookmodule/lab9_part2/deletebook_form.html', {'book': book})


# Homepage
def index(request):
    return render(request, 'index.html')

# Single book details
def one_book(request, bookId):
    book = get_object_or_404(Book, id=bookId)
    return render(request, 'bookmodule/lab9_part1/one_book.html', {'book': book})

# About us page
def about_us(request):
    return render(request, 'bookmodule/aboutus.html')

# HTML5 links page

def links_page(request):
    return render(request, 'bookmodule/html5/links.html')

# HTML5 formatting page
def formatting_page(request):
    return render(request, 'bookmodule/html5/formatting.html')

# HTML5 listing page
def listing_page(request):
    return render(request, 'bookmodule/html5/listing.html')

# HTML5 tables page
def tables_page(request):
    return render(request, 'bookmodule/html5/tables.html')

# Simple search
def search(request):
    query = request.GET.get('q', '')
    books = Book.objects.filter(Q(title__icontains=query) | Q(author__icontains=query))
    return render(request, 'bookmodule/search_results.html', {'books': books, 'query': query})

# Simple query example
def simple_query(request):
    avg_price = Book.objects.aggregate(Avg('price'))['price__avg']
    return HttpResponse(f"Average book price: {avg_price}")

# Complex query with lookups
def lookup_query(request):
    expensive_books = Book.objects.filter(price__gt=100)
    return render(request, 'bookmodule/lookup_results.html', {'books': expensive_books})
