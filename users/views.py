from django.urls import reverse_lazy
from django.views.generic import CreateView

from users.forms import UserRegistrationForm
from users.models import User


# Create your views here.
class UserCreateView(CreateView):
    model = User
    form_class = UserRegistrationForm
    success_url = reverse_lazy('users:login')
