from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .forms import CategoryForm, BookForm, ImportBooksForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from rest_framework.authtoken.models import Token
from django.shortcuts import redirect, render
from .models import Book, Category
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from utils.pandas import format_dataframe
from django.urls import reverse_lazy
import logging

logger = logging.getLogger(__name__)

# Create your views here.

# Books CRUD


class BookListView(LoginRequiredMixin, ListView):
    model = Book
    paginate_by = 25

    def get_queryset(self):
        return Book.objects.prefetch_related('category').order_by('-id')


class BookDetailView(LoginRequiredMixin, DetailView):
    model = Book

    def get_queryset(self):
        qs = super().get_queryset()
        return qs.prefetch_related('category')


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
        return Category.objects.prefetch_related('books')


class CategoryDetailView(LoginRequiredMixin, DetailView):
    model = Category

    def get_queryset(self):
        qs = super().get_queryset()
        return qs.prefetch_related('books')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        paginator = Paginator(self.object.books.all(), 25)
        page = self.request.GET.get('page')

        try:
            paginated_books = paginator.page(page)
        except PageNotAnInteger:
            paginated_books = paginator.page(1)
        except EmptyPage:
            paginated_books = paginator.page(paginator.num_pages)

        # Add the paginated books to the context
        context['page_obj'] = paginated_books
        return context


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


@login_required
def report(request):
    pass


@login_required
def import_books(request):
    if request.method == 'POST':
        form = ImportBooksForm(request.POST, request.FILES)
        if form.is_valid():
            books = Book.objects.all()
            books = list(books.values_list('book_id', flat=True))

            # Process the uploaded file to make a Json
            import json
            file = form.cleaned_data['file']
            logger.debug(
                f'Duplicatd per title: {file.duplicated(subset=["title", "category"]).sum()}')
            # file = file.drop_duplicates(
            #     subset=['id'], keep='first')
            file = format_dataframe(file)
            json_data = json.loads(file.to_json(orient='records'))
            # Make a request to the api to create the books
            import requests
            token = Token.objects.get(user=request.user)
            response = requests.post(
                url='http://172.21.0.1:80/api/v1/import-books',
                json=json_data,
                headers={'Authorization': f'Token {token.key}'}
            )

            logger.debug(
                f'Status: {response.status_code} Reason: {response.reason}')
            logger.debug(response.json())
            # Redirect to the book list page
            return redirect(reverse_lazy('books:index'))
    else:
        form = ImportBooksForm()
    return render(request, 'books/import_books_form.html', {'form': form})
