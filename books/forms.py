from django.core.validators import FileExtensionValidator
from django.core.exceptions import ValidationError
from .models import Category, Book, Expense
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit
from utils.pandas import validate_cols
from django import forms


class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ['name']

    def __init__(self, *args, **kwargs):
        super(CategoryForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.add_input(Submit('submit', 'Submit'))


class BookForm(forms.ModelForm):
    authors = forms.CharField(
        label='Authors',
        max_length=255,
        widget=forms.TextInput(attrs={'placeholder': 'Author1, Author2'}),
    )

    class Meta:
        model = Book
        fields = ['title', 'subtitle', 'category', 'authors',
                  'publisher', 'published_date', 'expense']
        widgets = {
            'published_date': forms.DateInput(
                attrs={'type': 'date', 'class': 'form-control'}
            ),
            'expense': forms.NumberInput(attrs={'step': '0.01'}),
        }

    def __init__(self, *args, **kwargs):
        super(BookForm, self).__init__(*args, **kwargs)
        # Adding crispy forms helper
        self.helper = FormHelper()
        self.helper.add_input(Submit('submit', 'Submit'))


class ImportBooksForm(forms.Form):
    file = forms.FileField(
        label='Books Data',
        validators=[
            FileExtensionValidator(allowed_extensions=['csv'])],
        help_text='Upload a .xlsx file with the books data.',
        required=True,
        allow_empty_file=False,
        widget=forms.ClearableFileInput(
            attrs={'accept': '.csv', 'class': 'form-control'}),
    )

    def __init__(self, *args, **kwargs):
        super(ImportBooksForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()

    def clean_file(self):
        # Check if the uploaded file is a valid spreadsheet

        COLS = [
            'title', 'subtitle', 'category', 'authors', 'publisher', 'published_date', 'distribution_expense'
        ]

        file = self.cleaned_data['file']
        try:
            import pandas as pd
            file = pd.read_csv(
                file,
                dtype=str,
                usecols=COLS,
                encoding='utf-8',
            )

            file.rename(
                columns={'distribution_expense': 'expense'}, inplace=True)
        except ValueError:
            raise ValidationError(f'Invalid file format or columns')

        return file
