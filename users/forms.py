from django.contrib.auth.forms import UserCreationForm

from catalog.forms import StyleFormMixin
from users.models import User


class UserRegistrationForm(UserCreationForm, StyleFormMixin):
    class Meta:
        model = User
        fields = ['email', 'first_name', 'last_name', 'password1', 'password2', 'avatar', 'phone', 'country']
