from django.urls import path
from . import views

urlpatterns = [
    path('import-books', views.BulkBookCreateView.as_view(),
         name='api_import_books'),
    path(
        'create-category',
        views.CategoryCreateAPIView.as_view(),
        name='api_create_category'
    ),
]
