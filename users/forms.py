from django.contrib.auth.forms import UserCreationForm
from django.forms import ModelForm

from catalog.forms import StyleFormMixin
from users.models import User


class UserRegistrationForm(StyleFormMixin, UserCreationForm):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email', 'password1', 'password2', 'avatar', 'phone', 'country']


# class PasswordRecoveryForm(StyleFormMixin, ModelForm):
#     class Meta:
#         model = User
#         fields = ['email']
