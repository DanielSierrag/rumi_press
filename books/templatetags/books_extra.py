from django import template
from books.models import Book
from django.db.models import Sum

register = template.Library()


@register.filter
def total_expenses(category):
    """
    Returns the total expenses for a given category.
    """
    return Book.objects.filter(category=category).aggregate(Sum('expense'))['expense__sum'] or 0
