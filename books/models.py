from django.db import models
from django.core.validators import MinLengthValidator

# Create your models here.


class Category(models.Model):
    name = models.CharField(max_length=100, unique=True)

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
        max_length=400,
        validators=[MinLengthValidator(2)]
    )
    subtitle = models.CharField(max_length=500, blank=True, null=True)
    authors = models.CharField(
        max_length=500,
        validators=[MinLengthValidator(2)]
    )
    publisher = models.CharField(
        max_length=150,
        validators=[MinLengthValidator(3)]
    )
    published_date = models.DateField()
    category = models.ForeignKey(
        Category, on_delete=models.CASCADE,
        related_name='books', null=True, blank=True
    )
    expense = models.DecimalField(
        max_digits=7, decimal_places=2, null=True, blank=True
    )

    def __str__(self):
        return self.title
