from django import forms
from django_registration.forms import RegistrationForm as BaseRegistrationForm
from .models import User
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit


class RegistrationForm(BaseRegistrationForm):
    username = None
    """
    Custom registration form that uses the User model.
    """
    class Meta(BaseRegistrationForm.Meta):
        model = User
        fields = ('email', 'password1', 'password2')

    def __init__(self, *args, **kwargs):
        super(RegistrationForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.add_input(Submit('submit', 'Register'))
