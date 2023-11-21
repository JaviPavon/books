from django.forms import formset_factory
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy

from django.utils import timezone

from django.views import View

from django.views.generic import (
    ListView,
    DetailView,
    DeleteView,
    UpdateView,
    CreateView,
)

from .models import Book

from .forms import BookForm


class ListBookView(ListView):
    model = Book


class DetailBookView(DetailView):
    model = Book


class BookCreate(CreateView):
    model = Book
    fields = ["title", "description", "rating", "author"]
    success_url = reverse_lazy("list_books")


class BookEdit(UpdateView):
    model = Book
    fields = ["title", "description", "rating", "author"]
    template_name_suffix = "_update_form"
    success_url = reverse_lazy("list_books")


class DeleteBookView(DeleteView):
    model = Book
    success_url = reverse_lazy("list_books")


class BookFormset(View):
    nombre_template = "books/book_formset.html"
    numero = Book.formularios
    numero_formularios = Book.objects.get(id=numero)

    def get(self, request):
        return render(
            request,
            self.nombre_template,
            context={"forms": formset_factory(BookForm, extra=self.numero_formularios)},
        )

    def post(self, request):
        formset = formset_factory(BookForm)
        formset = formset(data=request.POST)

        if formset.is_valid():
            for form in formset:
                if form.has_changed():
                    form.save()
            return redirect("list_books")

        else:
            return render(request, self.nombre_template, context={"forms": formset})


# class ListBooks(View):
#     nombre_template = 'books/list_books.html'
#     def get(self, request):
#         books = Book.objects.all()
#         return render(request, self.nombre_template, {'books': books})

# class DetailBookView(View):
#     def get(self, request, pk):
#         books = Book.objects.get(id=pk)
#         return render(request, 'books/book_detail.html', {'books': books})


# class BookCreate(View):

#     nombre_template = 'books/create_book.html'
#     books = Book.objects.filter(created_at__lte=timezone.now()).order_by('created_at')


#     def get(self, request):
#         form = BookForm()
#         return render(request, self.nombre_template, {'form': form, 'books': Book.objects.all()})

#     def post(self, request):
#         form = BookForm(request.POST)
#         if form.is_valid():
#             form.save()
#             return redirect('list_books')
#         return render(request, self.nombre_template, {'form':form, 'books': Book.objects.all()})


# class BookEdit(View):

#     nombre_template = 'books/edit_book.html'

#     def get(self, request, pk):
#         book = Book.objects.get(id=pk)
#         form = BookForm(instance=book)
#         return render(request, self.nombre_template, {'form': form, 'book': book})

#     def post(self, request, pk):
#         book = Book.objects.get(id=pk)
#         form = BookForm(request.POST, instance=book)
#         if form.is_valid():
#             form.save()
#             return redirect('list_books')
#         return render(request, self.nombre_template, {'form':form, 'book': book})


# class DeleteBookView(View):
#     nombre_template = 'books/book_confirm_delete.html'
#     def get(self, request, pk):
#         book = Book.objects.get(id=pk)
#         return render(request, self.nombre_template, {'book': book})
#     def post(self,  request,pk):
#         book = get_object_or_404(Book, id=pk)
#         book.delete()
#         return redirect('list_books')
