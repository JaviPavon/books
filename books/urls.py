from django.urls import path

from .views import ListBookView, DetailBookView, BookCreate, BookEdit, DeleteBookView, BookFormset

urlpatterns = [

path('', ListBookView.as_view(), name='list_books'),
path('book/<int:pk>/', DetailBookView.as_view(), name='book_details'),
path('book/create/', BookCreate.as_view(), name='book_creation'),
path('book/edit/<int:pk>', BookEdit.as_view(), name='book_edit'),
path('book/delete/<int:pk>', DeleteBookView.as_view(), name='book_delete'),
path('book/create4/', BookFormset.as_view(), name='book_creation4'),

]