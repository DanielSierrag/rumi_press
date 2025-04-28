from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.shortcuts import render
from django.urls import reverse_lazy
from .models import Book, Category
from .forms import CategoryForm, BookForm

# Create your views here.

# Books CRUD


class BookListView(ListView):
    model = Book

    def get_queryset(self):
        return Book.objects.prefetch_related('category')


class BookDetailView(DetailView):
    model = Book

    def get_queryset(self):
        qs = super().get_queryset()
        return qs.prefetch_related('category', 'expense', 'authors')


class BookCreateView(CreateView):
    model = Book
    form_class = BookForm
    success_url = reverse_lazy('books:index')


class BookUpdateView(UpdateView):
    model = Book
    form_class = BookForm
    success_url = reverse_lazy('books:index')


class BookDeleteView(DeleteView):
    model = Book
    template_name = 'books/object_confirm_delete.html'
    success_url = reverse_lazy('books:index')


# categories CRUD


class CategoryListView(ListView):
    model = Category

    def get_queryset(self):
        return Category.objects.prefetch_related('books', 'expenses')


class CategoryDetailView(DetailView):
    model = Category

    def get_queryset(self):
        qs = super().get_queryset()
        return qs.prefetch_related('books')


class CategoryCreateView(CreateView):
    model = Category
    form_class = CategoryForm
    success_url = reverse_lazy('books:category_list')


class CategoryUpdateView(UpdateView):
    model = Category
    form_class = CategoryForm
    success_url = reverse_lazy('books:category_list')


class CategoryDeleteView(DeleteView):
    model = Category
    template_name = 'books/object_confirm_delete.html'
    success_url = reverse_lazy('books:category_list')

# report views
