from django.shortcuts import render, redirect

from django.utils import timezone

from django.views import View

from .models import Book

from .forms import BookForm
 
class ListBooks(View):
    nombre_template = 'books/list_books.html'
    def get(self, request):
        books = Book.objects.all()
        return render(request, self.nombre_template, {'books': books})

class BookDetails(View):
    def get(self, request, pk):
        books = Book.objects.get(id=pk)
        return render(request, 'books/details_book.html', {'books': books})
    
class BookCreate(View):
    
    nombre_template = 'books/create_book.html'
    books = Book.objects.filter(created_at__lte=timezone.now()).order_by('created_at')

        
    def get(self, request):
        form = BookForm()
        return render(request, self.nombre_template, {'form': form, 'books': Book.objects.all()})

    def post(self, request):
        form = BookForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('list_books')
        return render(request, self.nombre_template, {'form':form, 'books': Book.objects.all()})
    
class BookEdit(View):
    
    nombre_template = 'books/edit_book.html'
        
    def get(self, request, pk):
        book = Book.objects.get(id=pk)
        form = BookForm(instance=book)
        return render(request, self.nombre_template, {'form': form, 'book': book})

    def post(self, request, pk):
        book = Book.objects.get(id=pk)
        form = BookForm(request.POST, instance=book)
        if form.is_valid():
            form.save()
            return redirect('list_books')
        return render(request, self.nombre_template, {'form':form, 'book': book})
