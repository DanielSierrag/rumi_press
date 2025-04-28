from django.db import models
from django.core.validators import MinLengthValidator

# Create your models here.


class Author(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Category(models.Model):
    name = models.CharField(max_length=100)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class Expense(models.Model):
    value = models.DecimalField(max_digits=7, decimal_places=2)
    category = models.ForeignKey(
        Category, on_delete=models.CASCADE, related_name='expenses'
    )

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.value)


class Book(models.Model):
    title = models.CharField(
        max_length=200,
        validators=[MinLengthValidator(3)]
    )
    subtitle = models.CharField(max_length=200, blank=True, null=True)
    authors = models.ManyToManyField(Author, related_name='books')
    publisher = models.CharField(
        max_length=150,
        validators=[MinLengthValidator(3)]
    )
    published_date = models.DateField()
    category = models.ForeignKey(
        Category, on_delete=models.CASCADE,
        related_name='books', null=True, blank=True
    )
    expense = models.OneToOneField(
        Expense, on_delete=models.CASCADE, related_name='book'
    )

    def __str__(self):
        return self.title
