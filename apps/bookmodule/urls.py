from django.urls import path
from . import views  # Import views from the current app

urlpatterns = [
    path('', views.index, name="books.index"),  # Homepage
    path('list_books/', views.list_books, name="books.list_books"),  # Books list page
    path('<int:bookId>/', views.one_book, name="books.one_book"),  # Single book details
    path('aboutus/', views.about_us, name="books.aboutus"),  # About us page
]
