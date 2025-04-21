from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('', views.index, name="books.index"),  # Homepage
    path('list_books/', views.list_books, name="books.list_books"),  # Books list page
    path('book/ <int:bookId>/', views.one_book, name="books.one_book"),  # Single book details
    path('aboutus/', views.about_us, name="books.aboutus"),  # About us page
    path('html5/links', views.links_page, name='links_page'),
    path('html5/text/formatting/', views.formatting_page, name='formatting_page'),
    path('html5/listing/', views.listing_page, name='listing_page'),
    path('html5/tables/', views.tables_page, name='tables_page'),
    path('search/', views.search, name='search'),
    path("simple/query/", views.simple_query, name="simple_query"), 
    path("complex/query/", views.lookup_query, name="lookup_query"),
    path('lab9/task1', views.task1),
    path('lab9/task2', views.task2),
    path('lab9/task3', views.task3),
    path('lab9/task4', views.task4),


    path('lab9_part1/listbooks', views.list_books, name='list_books'),
    path('lab9_part1/addbook', views.addbook, name='addbook'),
    path('lab9_part1/editbook/<int:id>', views.editbook, name='editbook'),
    path('lab9_part1/deletebook/<int:id>', views.deletebook, name='deletebook'),

    path('lab9_part2/listbooks', views.list_books_form, name='list_books_form'),
    path('lab9_part2/addbook', views.addbook_form, name='addbook_form'),
    path('lab9_part2/editbook/<int:id>/', views.editbook_form, name='editbook_form'),
    path('lab9_part2/deletebook/<int:id>/', views.deletebook_form, name='deletebook_form'),


]
