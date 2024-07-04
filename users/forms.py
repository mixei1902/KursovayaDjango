from django.contrib.auth.forms import UserCreationForm, UserChangeForm

from .models import CustomUser


class UserRegisterForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = ('email', 'phone', 'avatar', 'password1', 'password2')


class UserProfileForm(UserChangeForm):
    class Meta:
        model = CustomUser
        fields = ('email', 'phone', 'avatar')
