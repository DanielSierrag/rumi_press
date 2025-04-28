from .models import Category, Book, Expense
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit
from django import forms

import logging


class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ['name']

    def __init__(self, *args, **kwargs):
        super(CategoryForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.add_input(Submit('submit', 'Submit'))


class BookForm(forms.ModelForm):
    expense = forms.DecimalField(
        label='Expense',
        decimal_places=2, max_digits=7,
        widget=forms.NumberInput(attrs={'step': '0.01'}),
    )

    class Meta:
        model = Book
        fields = ['title', 'subtitle', 'category', 'authors',
                  'publisher', 'published_date']
        widgets = {
            'published_date': forms.DateInput(
                attrs={'type': 'date', 'class': 'form-control'}
            ),
            'authors': forms.CheckboxSelectMultiple(),
        }

    def __init__(self, *args, **kwargs):
        super(BookForm, self).__init__(*args, **kwargs)
        # Adding crispy forms helper
        self.helper = FormHelper()
        self.helper.add_input(Submit('submit', 'Submit'))

        # Managing data saving
    def save(self, commit=True):
        instance = super().save(commit=False)

        # Create or update expense related object
        expense_value = self.cleaned_data.get('expense')
        # If instance is not saved yet, we don't have an expense id
        expense_id = instance.expense.id if instance.pk else None
        expense, created = Expense.objects.update_or_create(
            pk=expense_id,
            defaults={'value': expense_value, 'category': instance.category},
            create_defaults={
                'value': expense_value, 'category': instance.category
            },
        )

        # Assign the expense to the book instance
        instance.expense = expense
        # Save instance
        if commit:
            instance.save()

        # Save the many-to-many relationship
        if 'authors' in self.cleaned_data:
            self.save_m2m()

        return instance
