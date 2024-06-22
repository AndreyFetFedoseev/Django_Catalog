import secrets

from django.contrib.auth.forms import PasswordResetForm
from django.contrib.auth.views import PasswordResetView
from django.core.mail import send_mail
from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse_lazy, reverse
from django.views.generic import CreateView

from config.settings import EMAIL_HOST_USER
from users.forms import UserRegistrationForm
from users.models import User


# Create your views here.
class UserCreateView(CreateView):
    model = User
    form_class = UserRegistrationForm
    success_url = reverse_lazy('users:login')

    def form_valid(self, form):
        user = form.save()
        user.is_active = False
        token = secrets.token_hex(16)
        user.token = token
        user.save()
        host = self.request.get_host()
        url = f'http://{host}/users/email_confirm/{token}/'
        send_mail(
            subject='Подтверждение почты',
            message=f'Для завершения регистрации пройдите по ссылке {url}',
            from_email=EMAIL_HOST_USER,
            recipient_list=[user.email]
        )
        return super().form_valid(form)


def get_verification(request, token):
    user = get_object_or_404(User, token=token)
    user.is_active = True
    user.save()
    return redirect(reverse('users:login'))


# class PasswordRecoveryView(PasswordResetView):
#     form_class = PasswordResetForm
#     template_name = 'users/password_recovery.html'
#     success_url = reverse_lazy('users:login')
#
#     def form_valid(self, form):
#         email = form.cleaned_data['email']
#         user = User.objects.get(email=email)
#         password = secrets.token_hex(8)
#         user.set_password(password)
#         user.save()
#         send_mail(
#             subject='Смена пароля',
#             message=f'Ваш новый пароль: {password}',
#             from_email=EMAIL_HOST_USER,
#             recipient_list=[user.email]
#         )
#         return redirect(reverse('users:login'))

def get_recovery_password(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        user = User.objects.get(email=email)
        password = secrets.token_hex(8)
        user.set_password(password)
        user.save()
        send_mail(
            subject='Смена пароля',
            message=f'Ваш новый пароль: {password}',
            from_email=EMAIL_HOST_USER,
            recipient_list=[user.email]
        )
    return render(request, 'users/get_recovery_password.html')
