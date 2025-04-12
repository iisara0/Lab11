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

    path('lab8/task1', views.task1),
    path('lab8/task2', views.task2),
    path('lab8/task3', views.task3),
    path('lab8/task4', views.task4),
    path('lab8/task5', views.task5),
    path('lab8/task7', views.task7),
]
