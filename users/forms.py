from django.contrib.auth.forms import UserCreationForm

from catalog.forms import StyleFormMixin
from users.models import User


class UserRegistrationForm(StyleFormMixin, UserCreationForm):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email', 'password1', 'password2', 'avatar', 'phone', 'country']
