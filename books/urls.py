from django.urls import path

from .views import ListBookView, DetailBookView, BookCreate, BookEdit

urlpatterns = [

path('', ListBookView.as_view(), name='list_books'),
path('book/<int:pk>/', DetailBookView.as_view(), name='book_details'),
path('book/create/', BookCreate.as_view(), name='book_creation'),
path('book/edit/<int:pk>', BookEdit.as_view(), name='book_edit'),
]