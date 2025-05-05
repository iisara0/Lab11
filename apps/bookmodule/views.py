from django.shortcuts import render ,get_object_or_404, redirect
from .models import Book , Address ,Department ,Course ,Students ,Students2
from django.db.models import Q, Count, Sum, Avg, Max, Min
from .forms import BookForm, StudentForm, Student2Form
from django.contrib.auth.decorators import login_required

#LAB12
@login_required
def book_list(request):
    return render(request, 'bookmodule//lab9_part1/list_books.html')

#Task 1 LAB11
def student_list(request):
    students = Students.objects.all()
    print(students)
    return render(request, 'bookmodule/lab11/student_list.html', {'students': students})

def student_create(request):
    if request.method == 'POST':
        form = StudentForm(request.POST)
        #form = Student2Form(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('student_list')
    else:
        form = StudentForm()
    return render(request, 'bookmodule/lab11/student_form.html', {'form': form})

def student_update(request, pk):
    student = get_object_or_404(Students, pk=pk)
    if request.method == 'POST':
        #form = StudentForm(request.POST, instance=student)
        form = Student2Form(request.POST, request.FILES)
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





from django.shortcuts import render, redirect, get_object_or_404
from .models import Students2
from .forms import Student2Form

def student2_list(request):
    students = Students2.objects.all()
    return render(request, 'bookmodule/lab11/student2_list.html', {'students': students})

def student2_create(request):
    if request.method == 'POST':
        form = Student2Form(request.POST, request.FILES)
        if form.is_valid():
            form.save()  # This already handles everything
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



def list_books(request):
    books = Book.objects.all()
    return render(request, 'bookmodule/lab9_part1/list_books.html', {'books': books})

def addbook(request):
    if request.method == 'POST':
        title = request.POST['title']
        author = request.POST['author']
        price = float(request.POST['price'])
        edition = int(request.POST['edition'])
        Book.objects.create(title=title, author=author, price=price, edition=edition)
        return redirect('list_books')

    return render(request, 'bookmodule/lab9_part1/addbook.html')



def editbook(request, id):
    book = Book.objects.get(id=id)
    if request.method == 'POST':
        book.title = request.POST['title']
        book.author = request.POST['author']
        book.price = float(request.POST['price'])
        book.edition = int(request.POST['edition'])
        book.save()
        return redirect('list_books')

    return render(request, 'bookmodule/lab9_part1/editbook.html', {'book': book})


def deletebook(request, id):
    book = Book.objects.get(id=id)
    book.delete()
    return redirect('list_books')




# def student2_list(request):
#     books = Book.objects.all()
#     return render(request, 'bookmodule/lab9_part2/student2_list.html', {'books': books})


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







def task1(request):
    departments = Department.objects.annotate(student_count=Count('student'))
    return render(request, 'bookmodule/task1.html', {'departments': departments})



def task2(request):
    courses = Course.objects.annotate(student_count=Count('student'))
    return render(request, 'bookmodule/task2.html', {'courses': courses})


def task3(request):
    
    departments = Department.objects.annotate( min_card_id=Min('student__card__id') )


    oldest_students = []
    for dept in departments:
        
        if dept.min_card_id is not None:
            
            student = dept.student.filter(card__id=dept.min_card_id).first()
            if student:
                oldest_students.append((dept.name, student.name))
        else:
            oldest_students.append((dept.name, "No students"))

    return render(request, 'bookmodule/task3.html', {'oldest_students': oldest_students})



def task4(request):
    departments = Department.objects.annotate(student_count=Count('student')).filter(student_count__gt=2).order_by('-student_count')
    return render(request, 'bookmodule/task4.html', {'departments': departments})


# def task1(request):
#     books = Book.objects.filter(Q(price__gte=80))
#     return render(request, 'bookmodule/task1.html', {'books': books})


# def task2(request):
#     books = Book.objects.filter(
#         Q(edition__gt=3) & (Q(title__icontains='co') | Q(author__icontains='co'))
#     )
#     return render(request, 'bookmodule/task2.html', {'books': books})


# def task3(request):
#     books = Book.objects.filter(
#         Q(edition__lte=3) & ~Q(title__icontains='co') & ~Q(author__icontains='co')
#     )
#     return render(request, 'bookmodule/task3.html', {'books': books})


# def task4(request):
#     books = Book.objects.all().order_by('title')
#     return render(request, 'bookmodule/task4.html', {'books': books})


def task5(request):
    stats = Book.objects.aggregate(
        total_books=Count('id'),
        total_price=Sum('price'),
        avg_price=Avg('price'),
        max_price=Max('price'),
        min_price=Min('price'),
    )
    return render(request, 'bookmodule/task5.html', {'stats': stats})

def task7(request):
    city = Address.objects.annotate(student_count=Count('student'))
    city_with_students = city.filter(student_count__gt=0)
    
    return render(request, 'bookmodule/task7.html', {'city': city_with_students})


def index(request):
    return render(request, 'bookmodule/index.html')


# def list_books(request):
#     return render(request, 'bookmodule/list_books.html')


def about_us(request):
    return render(request, 'bookmodule/aboutus.html')


def one_book(request, bookId):
    return render(request, 'bookmodule/one_book.html')


def links_page(request):
    return render(request, 'bookmodule/html5/links.html')


def formatting_page(request):
    return render(request, 'bookmodule/html5/text/formatting.html')


def listing_page(request):
    return render(request, 'bookmodule/html5/listing.html')


def tables_page(request):
    return render(request, 'bookmodule/html5/tables.html')


def search(request):
    books = __getBooksList()
    newBooks = []

    if request.method == "POST":
        string = request.POST.get('keyword', '').strip().lower()
        isTitle = request.POST.get('option1')
        isAuthor = request.POST.get('option2')

        if string:
            for item in books:
                contained = False
                if isTitle and string in item['title'].lower():
                    contained = True
                if not contained and isAuthor and string in item['author'].lower():
                    contained = True
                if contained:
                    newBooks.append(item)

        return render(request, 'bookmodule/bookList.html', {'books': newBooks})

    return render(request, 'bookmodule/search.html')


def __getBooksList():
    return [
        {'id': 12344321, 'title': 'Continuous Delivery', 'author': 'J.Humble and D. Farley'},
        {'id': 56788765, 'title': 'Reversing: Secrets of Reverse Engineering', 'author': 'E. Eilam'},
        {'id': 43211234, 'title': 'The Hundred-Page Machine Learning Book', 'author': 'Andriy Burkov'},
    ]


def simple_query(request):
    mybooks = Book.objects.filter(title__icontains='and')
    return render(request, 'bookmodule/bookList.html', {'books': mybooks})


def lookup_query(request):
    mybooks = Book.objects.filter(
        author__isnull=False
    ).filter(
        title__icontains='and'
    ).filter(
        edition__gte=2
    ).exclude(
        price__lte=100
    )[:10]

    if mybooks.exists():
        return render(request, 'bookmodule/bookList.html', {'books': mybooks})
    else:
        return render(request, 'bookmodule/index.html')


def create_book(request):
    book = Book.objects.create(title='Continuous Delivery', author='J.Humble and D. Farley', edition=1)
    return render(request, 'bookmodule/book_created.html', {'book': book})
