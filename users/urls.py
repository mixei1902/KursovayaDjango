from django.contrib.auth import views as auth_views
from django.urls import path

from .views import UserCreateView, email_verification, reset_password, ProfileView, UserListView, toggle_activity

app_name = 'users'

urlpatterns = [
    path('login/', auth_views.LoginView.as_view(template_name='users/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(next_page='home'), name='logout'),
    path('register/', UserCreateView.as_view(), name='register'),
    path('email-confirm/<str:token>/', email_verification, name='email_confirm'),
    path('reset-password/', reset_password, name='reset_password'),
    path('profile/', ProfileView.as_view(), name='profile'),
    path('users-list/', UserListView.as_view(), name='users_list'),
    path('toggle-activity/<int:pk>/', toggle_activity, name='toggle_activity'),
]
