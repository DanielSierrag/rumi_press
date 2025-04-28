"""
URL configuration for rumi_press project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django_registration.backends.one_step.views import RegistrationView
from books_auth.forms import RegistrationForm
from django.views.generic import TemplateView
from django.urls import path, include
from django.contrib import admin
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path(
        'accounts/register/',
        RegistrationView.as_view(form_class=RegistrationForm),
        name='django_registration_register'
    ),
    path(
        'accounts/profile/',
        TemplateView.as_view(template_name='registration/profile.html'),
        name='profile'
    ),
    path('accounts/', include('django_registration.backends.one_step.urls')),
    path('accounts/', include('django.contrib.auth.urls')),
    path('', views.home, name='home'),
    path('books/', include('books.urls')),
]
