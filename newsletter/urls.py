from django.urls import path
from .views import (
    ClientListView, ClientDetailView, ClientCreateView, ClientUpdateView, ClientDeleteView,
    MessageListView, MessageDetailView, MessageCreateView, MessageUpdateView, MessageDeleteView,
    MailingListView, MailingDetailView, MailingCreateView, MailingUpdateView, MailingDeleteView,
    ReportListView, ReportDetailView, UserCreateView, UserDeleteView, UserUpdateView
)

urlpatterns = [
    path('clients/', ClientListView.as_view(), name='client_list'),
    path('clients/<int:pk>/', ClientDetailView.as_view(), name='client_detail'),
    path('clients/new/', ClientCreateView.as_view(), name='client_create'),
    path('clients/<int:pk>/edit/', ClientUpdateView.as_view(), name='client_update'),
    path('clients/<int:pk>/delete/', ClientDeleteView.as_view(), name='client_delete'),

    path('messages/', MessageListView.as_view(), name='message_list'),
    path('messages/<int:pk>/', MessageDetailView.as_view(), name='message_detail'),
    path('messages/new/', MessageCreateView.as_view(), name='message_create'),
    path('messages/<int:pk>/edit/', MessageUpdateView.as_view(), name='message_update'),
    path('messages/<int:pk>/delete/', MessageDeleteView.as_view(), name='message_delete'),

    path('mailings/', MailingListView.as_view(), name='mailing_list'),
    path('mailings/<int:pk>/', MailingDetailView.as_view(), name='mailing_detail'),
    path('mailings/new/', MailingCreateView.as_view(), name='mailing_create'),
    path('mailings/<int:pk>/edit/', MailingUpdateView.as_view(), name='mailing_update'),
    path('mailings/<int:pk>/delete/', MailingDeleteView.as_view(), name='mailing_delete'),

    path('reports/', ReportListView.as_view(), name='report_list'),
    path('reports/<int:pk>/', ReportDetailView.as_view(), name='report_detail'),

    path('users/new/', UserCreateView.as_view(), name='user_create'),
    path('users/<int:pk>/edit/', UserUpdateView.as_view(), name='user_update'),
    path('users/<int:pk>/delete/', UserDeleteView.as_view(), name='user_delete'),
]
