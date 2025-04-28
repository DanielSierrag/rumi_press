from django.urls import path
from . import views

app_name = 'books'

urlpatterns = [
    # Books CRUD
    path('', views.index, name='index'),
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
