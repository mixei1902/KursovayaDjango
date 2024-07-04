from django.urls import path

from .views import UserCreateView, email_verification, reset_password, ProfileView, UserListView, toggle_activity

app_name = 'users'

urlpatterns = [
    path('register/', UserCreateView.as_view(), name='register'),
    path('email-confirm/<str:token>/', email_verification, name='email_confirm'),
    path('reset-password/', reset_password, name='reset_password'),
    path('profile/', ProfileView.as_view(), name='profile'),
    path('users-list/', UserListView.as_view(), name='users_list'),
    path('toggle-activity/<int:pk>/', toggle_activity, name='toggle_activity'),
]
