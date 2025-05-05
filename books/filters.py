"""
This module contains filters for processing book, expenses and categories data in the view.
"""

from django import forms
from .models import Category, Book
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
    category = django_filters.MultipleChoiceFilter(
        field_name="category",
        choices=[
            (cid, name) for cid, name in Category.objects.values_list('id', 'name').distinct()
        ],
        label="Category",
        widget=forms.CheckboxSelectMultiple(attrs={
            'class': 'form-check-input',
        }),
    )


class CategoriesFilter(django_filters.FilterSet):
    name = django_filters.MultipleChoiceFilter(
        field_name="name",
        choices=[
            (name, name) for name in Category.objects.values_list('name', flat=True).distinct()
        ],
        label="Category",
        widget=forms.CheckboxSelectMultiple(attrs={
            'class': 'form-check-input',
        }),
    )
