from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.shortcuts import render
from django.urls import reverse_lazy
from .models import Book, Category
from .forms import CategoryForm

# Create your views here.


def index(request):
    return render(request, 'books/index.html', {})

# Books CRUD


# class BookListView(ListView):
#     model = Book


# categories CRUD


class CategoryListView(ListView):
    model = Category

    def get_queryset(self):
        return Category.objects.prefetch_related('books', 'expenses').all()


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
