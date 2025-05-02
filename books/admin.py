from django.contrib import admin
from . import models

# Register your models here.


@admin.register(models.Book)
class BookAdmin(admin.ModelAdmin):
    list_display = [
        field.name for field in models.Book._meta.fields if field.name not in ['id', 'authors']
    ]
    search_fields = ('title', 'publisher', 'subtitle', 'authors')
    list_filter = ('category', 'published_date')


admin.site.register(models.Category)
