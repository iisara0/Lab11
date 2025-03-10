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

def links_page(request):
    return render(request, 'bookmodule/html5/links.html')

def formatting_page(request):
    return render(request, 'bookmodule/html5/text/formatting.html')

def listing_page(request):
    return render(request, 'bookmodule/html5/listing.html')

def tables_page(request):
    return render(request, 'bookmodule/html5/tables.html')

#def search(request):
    #return render(request, 'bookmodule/search.html')

def search(request):
    books = __getBooksList()  # Fetch books
    newBooks = []  # Store filtered books

    if request.method == "POST":
        string = request.POST.get('keyword', '').strip().lower()
        isTitle = request.POST.get('option1')
        isAuthor = request.POST.get('option2')

        # If the user enters a keyword, filter the books
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
    book1 = {'id':12344321, 'title':'Continuous Delivery', 'author':'J.Humble and D. Farley'}
    book2 = {'id':56788765,'title':'Reversing: Secrets of Reverse Engineering', 'author':'E. Eilam'}
    book3 = {'id':43211234, 'title':'The Hundred-Page Machine Learning Book', 'author':'Andriy Burkov'}
    return [book1, book2, book3]

