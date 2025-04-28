from django.urls import reverse
from django.shortcuts import render, redirect


def home(request):
    return redirect(reverse('books:index'))
