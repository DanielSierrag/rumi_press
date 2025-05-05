"""
This module contains filters for processing book, expenses and categories data in the view.
"""

from .forms import BookFilterForm
from .models import Book
from django import forms
import django_filters


class BookFilter(django_filters.FilterSet):
    title = django_filters.CharFilter(
        field_name="title",
        lookup_expr="icontains",
        label="Title",
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': ' Book title...'
        })
    )
    subtitle = django_filters.CharFilter(
        field_name="subtitle",
        lookup_expr="icontains",
        label="Subtitle",
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': ' Book subtitle...'
        })
    )
    authors = django_filters.CharFilter(
        field_name="authors",
        lookup_expr="icontains",
        label="Author 1, Author 2...",
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': ' Book authors...'
        })
    )
    publisher = django_filters.CharFilter(
        field_name="publisher",
        lookup_expr="icontains",
        label="Publisher",
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': ' Book publisher...'
        })
    )
    published_date__gt = django_filters.DateFilter(
        field_name="published_date",
        lookup_expr="gt",
        label="Published After",
        widget=forms.DateInput(attrs={
            'class': 'form-control',
            'type': 'date',
        })
    )
    published_date__lt = django_filters.DateFilter(
        field_name="published_date",
        lookup_expr="lt",
        label="Published Before",
        widget=forms.DateInput(attrs={
            'class': 'form-control',
            'type': 'date',
        })
    )

    # class Meta:
    #     model=Book
    #     # fields = ['title', 'subtitle', 'authors',
    #     #           'category', 'publisher', 'published_date']
    #     fields={
    #         'title': ['icontains'],
    #         'subtitle': ['icontains'],
    #         'authors': ['icontains'],
    #         'category': ['exact'],
    #         'publisher': ['icontains'],
    #         'published_date': ['exact'],
    #     }
    #     exclude=['title', 'published_date']
    # form = BookFilterForm
