from django import template
from books.models import Expense
from django.db.models import Sum

register = template.Library()


@register.simple_tag
def book_authors(book):
    """
    Returns a comma-separated string of all authors of a book instance.
    """
    return ", ".join(author.name for author in book.authors.all())


@register.filter
def total_expenses(category):
    """
    Returns the total expenses for a given category.
    """
    return Expense.objects.filter(category=category).aggregate(total=Sum('value'))['total'] or 0
