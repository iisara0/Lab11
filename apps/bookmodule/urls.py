from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('', views.index, name="books.index"),  # Homepage
    path('list_books/', views.list_books, name="books.list_books"),  # Books list page
    path('<int:bookId>/', views.one_book, name="books.one_book"),  # Single book details
    path('aboutus/', views.about_us, name="books.aboutus"),  # About us page
    path('html5/links', views.links_page, name='links_page'),
    path('html5/text/formatting/', views.formatting_page, name='formatting_page'),
    path('html5/listing/', views.listing_page, name='listing_page'),
    path('html5/tables/', views.tables_page, name='tables_page'),

]
