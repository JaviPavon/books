from django.urls import path

from .views import ListBooks, BookDetails, BookCreate, BookEdit

urlpatterns = [

path('', ListBooks.as_view(), name='list_books'),
path('book/<int:pk>/', BookDetails.as_view(), name='book_details'),
path('book/create/', BookCreate.as_view(), name='book_creation'),
path('book/edit/<int:pk>', BookEdit.as_view(), name='book_edit'),
]