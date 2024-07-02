from django import forms

from .models import Client, Message, Mailing


class ClientForm(forms.ModelForm):
    """
    Форма для создания и редактирования клиентов сервиса.
    """

    class Meta:
        model = Client
        fields = ['email', 'full_name', 'comment']


class MessageForm(forms.ModelForm):
    """
    Форма для создания и редактирования сообщений рассылки.
    """

    class Meta:
        model = Message
        fields = ['subject', 'body']


class MailingForm(forms.ModelForm):
    """
    Форма для создания и редактирования рассылок.
    """

    class Meta:
        model = Mailing
        fields = ['start_date', 'periodicity', 'status', 'message', 'clients']
        widgets = {
            'clients': forms.CheckboxSelectMultiple,
        }
