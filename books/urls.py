from django.urls import path
from . import views

app_name = 'books'

urlpatterns = [
    # Books CRUD
    path('', views.BookListView.as_view(), name='index'),
    path('<int:pk>/', views.BookDetailView.as_view(), name='book_detail'),
    path('create/', views.BookCreateView.as_view(), name='book_create'),
    path('<int:pk>/update/', views.BookUpdateView.as_view(), name='book_update'),
    path('<int:pk>/delete/', views.BookDeleteView.as_view(), name='book_delete'),
]

# Categories CRUD
urlpatterns += [
    path('categories/', views.CategoryListView.as_view(), name='category_list'),
    path(
        'categories/<int:pk>/',
        views.CategoryDetailView.as_view(),
        name='category_detail'
    ),
    path(
        'categories/create/',
        views.CategoryCreateView.as_view(),
        name='category_create'
    ),
    path(
        'categories/<int:pk>/update/',
        views.CategoryUpdateView.as_view(),
        name='category_update'
    ),
    path(
        'categories/<int:pk>/delete/',
        views.CategoryDeleteView.as_view(),
        name='category_delete'
    ),
]

# Report views
urlpatterns += [
    path('import-books', views.import_books, name='import_books'),
    path('expenses-dashboard', views.expenses_dashboard, name='expenses_dashboard'),
]
