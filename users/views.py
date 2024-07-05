import random
import secrets
import string

from django.contrib.auth.decorators import permission_required
from django.contrib.auth.mixins import PermissionRequiredMixin
from django.core.mail import send_mail
from django.shortcuts import redirect, get_object_or_404, render
from django.urls import reverse, reverse_lazy
from django.views.generic import CreateView, UpdateView, ListView

from config.settings import EMAIL_HOST_USER
from .forms import UserRegisterForm, UserProfileForm
from .models import CustomUser


class UserCreateView(CreateView):
    model = CustomUser
    form_class = UserRegisterForm
    template_name = 'users/register.html'
    success_url = reverse_lazy('users:login')

    def form_valid(self, form):
        user = form.save()
        user.is_active = False
        token = secrets.token_hex(16)
        user.token = token
        user.save()
        host = self.request.get_host()
        url = f'http://{host}/users/email-confirm/{token}/'
        send_mail(subject="Подтверждение почты",
                  message=f"Перейдите по ссылке для подтверждения почты {url}",
                  from_email=EMAIL_HOST_USER,
                  recipient_list=[user.email])
        return super().form_valid(form)


def email_verification(request, token):
    user = get_object_or_404(CustomUser, token=token)
    user.is_active = True
    user.token = None
    user.save()
    return redirect(reverse('users:login'))


def reset_password(request):
    context = {
        'success_message': 'Пароль успешно сброшен. Новый пароль был отправлен на ваш адрес электронной почты.',
    }
    if request.method == 'POST':
        email = request.POST.get('email')
        user = get_object_or_404(CustomUser, email=email)
        characters = string.ascii_letters + string.digits
        password = ''.join(random.choice(characters) for _ in range(10))
        user.set_password(password)
        user.save()
        send_mail(subject='Восстановление пароля',
                  message=f'Здравствуйте, вы запрашивали обновление пароля. Ваш новый пароль: {password}',
                  from_email=EMAIL_HOST_USER,
                  recipient_list=[user.email])
        return render(request, 'users/reset_password.html', context)
    return render(request, 'users/reset_password.html')


class ProfileView(UpdateView):
    model = CustomUser
    form_class = UserProfileForm
    template_name = 'users/profile.html'
    success_url = reverse_lazy('users:profile')

    def get_object(self, queryset=None):
        return self.request.user


class UserListView(PermissionRequiredMixin, ListView):
    model = CustomUser
    template_name = 'users/user_list.html'
    permission_required = 'users.view_all_users'


@permission_required('users.deactivate_user')
def toggle_activity(request, pk):
    user = CustomUser.objects.get(pk=pk)
    user.is_active = not user.is_active
    user.save()
    return redirect(reverse('users:users_list'))
