from django.shortcuts import render
from .models import Book, Student, Address
from django.db.models import Q, Count, Sum, Avg, Max, Min


def task1(request):
    books = Book.objects.filter(Q(price__gte=80))
    return render(request, 'bookmodule/task1.html', {'books': books})


def task2(request):
    books = Book.objects.filter(
        Q(edition__gt=3) & (Q(title__icontains='co') | Q(author__icontains='co'))
    )
    return render(request, 'bookmodule/task2.html', {'books': books})


def task3(request):
    books = Book.objects.filter(
        Q(edition__lte=3) & ~Q(title__icontains='co') & ~Q(author__icontains='co')
    )
    return render(request, 'bookmodule/task3.html', {'books': books})


def task4(request):
    books = Book.objects.all().order_by('title')
    return render(request, 'bookmodule/task4.html', {'books': books})


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


def list_books(request):
    return render(request, 'bookmodule/list_books.html')


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
