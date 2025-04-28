from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from .models import Book, Category
from .forms import CategoryForm, BookForm

# Create your views here.

# Books CRUD


class BookListView(LoginRequiredMixin, ListView):
    model = Book

    def get_queryset(self):
        return Book.objects.prefetch_related('category')


class BookDetailView(LoginRequiredMixin, DetailView):
    model = Book

    def get_queryset(self):
        qs = super().get_queryset()
        return qs.prefetch_related('category', 'expense', 'authors')


class BookCreateView(LoginRequiredMixin, CreateView):
    model = Book
    form_class = BookForm
    success_url = reverse_lazy('books:index')


class BookUpdateView(LoginRequiredMixin, UpdateView):
    model = Book
    form_class = BookForm
    success_url = reverse_lazy('books:index')


class BookDeleteView(LoginRequiredMixin, DeleteView):
    model = Book
    template_name = 'books/object_confirm_delete.html'
    success_url = reverse_lazy('books:index')


# categories CRUD


class CategoryListView(LoginRequiredMixin, ListView):
    model = Category

    def get_queryset(self):
        return Category.objects.prefetch_related('books', 'expenses')


class CategoryDetailView(LoginRequiredMixin, DetailView):
    model = Category

    def get_queryset(self):
        qs = super().get_queryset()
        return qs.prefetch_related('books')


class CategoryCreateView(LoginRequiredMixin, CreateView):
    model = Category
    form_class = CategoryForm
    success_url = reverse_lazy('books:category_list')


class CategoryUpdateView(LoginRequiredMixin, UpdateView):
    model = Category
    form_class = CategoryForm
    success_url = reverse_lazy('books:category_list')


class CategoryDeleteView(LoginRequiredMixin, DeleteView):
    model = Category
    template_name = 'books/object_confirm_delete.html'
    success_url = reverse_lazy('books:category_list')

# report views
