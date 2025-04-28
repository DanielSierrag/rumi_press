from django.contrib import admin
from . import models

# Register your models here.


@admin.register(models.Book)
class BookAdmin(admin.ModelAdmin):
    list_display = [
        field.name for field in models.Book._meta.fields if field.name not in ['id', 'authors']
    ]
    search_fields = ('title', 'publisher', 'subtitle', 'authors__name')
    list_filter = ('category', 'published_date')


@admin.register(models.Expense)
class ExpenseAdmin(admin.ModelAdmin):
    list_display = ('value', 'category', 'book')
    search_fields = ('category__name', 'book__title')
    list_filter = ('book__category',)


admin.site.register(models.Category)
admin.site.register(models.Author)
