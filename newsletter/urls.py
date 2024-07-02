from django.urls import path
from .views import mailing_list, mailing_detail, mailing_create, mailing_update, mailing_delete

urlpatterns = [
    path('', mailing_list, name='mailing_list'),
    path('mailing/<int:pk>/', mailing_detail, name='mailing_detail'),
    path('mailing/new/', mailing_create, name='mailing_create'),
    path('mailing/<int:pk>/edit/', mailing_update, name='mailing_update'),
    path('mailing/<int:pk>/delete/', mailing_delete, name='mailing_delete'),
]
