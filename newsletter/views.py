from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.models import User
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

from .forms import ClientForm, MailingForm, MessageForm
from .models import Client, Mailing, MailingAttempt, Message


class ClientListView(LoginRequiredMixin, ListView):
    """
        Представление для отображения списка клиентов текущего пользователя.
     """
    model = Client
    template_name = 'newsletter/client_list.html'

    def get_queryset(self):
        return Client.objects.filter(owner=self.request.user)


class ClientDetailView(LoginRequiredMixin, DetailView):
    """
    Представление для отображения деталей клиента текущего пользователя.
    """
    model = Client
    template_name = 'newsletter/client_detail.html'

    def get_queryset(self):
        return Client.objects.filter(owner=self.request.user)


class ClientCreateView(LoginRequiredMixin, CreateView):
    """
    Представление для создания нового клиента.
    """
    model = Client
    form_class = ClientForm
    template_name = 'newsletter/client_form.html'
    success_url = reverse_lazy('client_list')

    def form_valid(self, form):
        form.instance.owner = self.request.user
        return super().form_valid(form)


class ClientUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    """
    Представление для редактирования существующего клиента.
    """
    model = Client
    form_class = ClientForm
    template_name = 'newsletter/client_form.html'
    success_url = reverse_lazy('client_list')

    def get_queryset(self):
        return Client.objects.filter(owner=self.request.user)

    def test_func(self):
        client = self.get_object()
        return client.owner == self.request.user


class ClientDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    """
    Представление для удаления клиента.
    """
    model = Client
    template_name = 'newsletter/client_confirm_delete.html'
    success_url = reverse_lazy('client_list')

    def get_queryset(self):
        return Client.objects.filter(owner=self.request.user)

    def test_func(self):
        client = self.get_object()
        return client.owner == self.request.user


class MailingListView(LoginRequiredMixin, ListView):
    """
    Представление для отображения списка рассылок текущего пользователя.
    """
    model = Mailing
    template_name = 'newsletter/mailing_list.html'

    def get_queryset(self):
        return Mailing.objects.filter(owner=self.request.user)


class MailingDetailView(LoginRequiredMixin, DetailView):
    """
    Представление для отображения деталей рассылки текущего пользователя.
    """
    model = Mailing
    template_name = 'newsletter/mailing_detail.html'

    def get_queryset(self):
        return Mailing.objects.filter(owner=self.request.user)


class MailingCreateView(LoginRequiredMixin, CreateView):
    """
    Представление для создания новой рассылки.
    """
    model = Mailing
    form_class = MailingForm
    template_name = 'newsletter/mailing_form.html'
    success_url = reverse_lazy('mailing_list')

    def form_valid(self, form):
        form.instance.owner = self.request.user
        return super().form_valid(form)


class MailingUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    """
    Представление для редактирования существующей рассылки.
    """
    model = Mailing
    form_class = MailingForm
    template_name = 'newsletter/mailing_form.html'
    success_url = reverse_lazy('mailing_list')

    def get_queryset(self):
        return Mailing.objects.filter(owner=self.request.user)

    def test_func(self):
        mailing = self.get_object()
        return mailing.owner == self.request.user


class MailingDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    """
    Представление для удаления рассылки.
    """
    model = Mailing
    template_name = 'newsletter/mailing_confirm_delete.html'
    success_url = reverse_lazy('mailing_list')

    def get_queryset(self):
        return Mailing.objects.filter(owner=self.request.user)

    def test_func(self):
        mailing = self.get_object()
        return mailing.owner == self.request.user


class ReportListView(LoginRequiredMixin, ListView):
    model = MailingAttempt
    template_name = 'newsletter/report_list.html'


class ReportDetailView(LoginRequiredMixin, DetailView):
    model = MailingAttempt
    template_name = 'newsletter/report_detail.html'


class UserCreateView(LoginRequiredMixin, CreateView):
    model = User
    form_class = UserCreationForm
    template_name = 'newsletter/user_form.html'
    success_url = reverse_lazy('user_list')


class UserUpdateView(LoginRequiredMixin, UpdateView):
    model = User
    form_class = UserChangeForm
    template_name = 'newsletter/user_form.html'
    success_url = reverse_lazy('user_list')


class UserDeleteView(LoginRequiredMixin, DeleteView):
    model = User
    template_name = 'newsletter/user_confirm_delete.html'
    success_url = reverse_lazy('user_list')


class MessageListView(LoginRequiredMixin, ListView):
    model = Message
    template_name = 'newsletter/message_list.html'

    def get_queryset(self):
        return Message.objects.filter(owner=self.request.user)


class MessageDetailView(LoginRequiredMixin, DetailView):
    model = Message
    template_name = 'newsletter/message_detail.html'

    def get_queryset(self):
        return Message.objects.filter(owner=self.request.user)


class MessageCreateView(LoginRequiredMixin, CreateView):
    model = Message
    form_class = MessageForm
    template_name = 'newsletter/message_form.html'
    success_url = reverse_lazy('message_list')

    def form_valid(self, form):
        form.instance.owner = self.request.user
        return super().form_valid(form)


class MessageUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Message
    form_class = MessageForm
    template_name = 'newsletter/message_form.html'
    success_url = reverse_lazy('message_list')

    def get_queryset(self):
        return Message.objects.filter(owner=self.request.user)

    def test_func(self):
        message = self.get_object()
        return message.owner == self.request.user


class MessageDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Message
    template_name = 'newsletter/message_confirm_delete.html'
    success_url = reverse_lazy('message_list')

    def get_queryset(self):
        return Message.objects.filter(owner=self.request.user)

    def test_func(self):
        message = self.get_object()
        return message.owner == self.request.user
