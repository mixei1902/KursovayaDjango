from django.urls import path

from . import views
from .views import client_list, client_detail, client_create, client_update, client_delete
from .views import mailing_list, mailing_detail, mailing_create, mailing_update, mailing_delete
from .views import message_list, message_detail, message_create, message_update, message_delete

app_name = 'newsletter'

urlpatterns = [
    # Clients
    path('clients/', client_list, name='client_list'),
    path('clients/<int:pk>/', client_detail, name='client_detail'),
    path('clients/new/', client_create, name='client_create'),
    path('clients/<int:pk>/edit/', client_update, name='client_update'),
    path('clients/<int:pk>/delete/', client_delete, name='client_delete'),

    # Messages
    path('messages/', message_list, name='message_list'),
    path('messages/<int:pk>/', message_detail, name='message_detail'),
    path('messages/new/', message_create, name='message_create'),
    path('messages/<int:pk>/edit/', message_update, name='message_update'),
    path('messages/<int:pk>/delete/', message_delete, name='message_delete'),

    # Mailings
    path('mailings/', mailing_list, name='mailing_list'),
    path('mailings/<int:pk>/', mailing_detail, name='mailing_detail'),
    path('mailings/new/', mailing_create, name='mailing_create'),
    path('mailings/<int:pk>/edit/', mailing_update, name='mailing_update'),
    path('mailings/<int:pk>/delete/', mailing_delete, name='mailing_delete'),
]
