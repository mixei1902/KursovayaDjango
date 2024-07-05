from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.views.generic import TemplateView

from blog.models import BlogPost
from .forms import ClientForm, MailingForm, MessageForm
from .models import Client, Mailing, MailingAttempt, Message


class HomePageView(TemplateView):
    template_name = 'newsletter/home.html'


class ClientListView(LoginRequiredMixin, ListView):
    """
        Представление для отображения списка клиентов текущего пользователя.
     """
    model = Client
    template_name = 'newsletter/client_list.html'
    context_object_name = 'clients'

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
    success_url = reverse_lazy('newsletter:client_list')

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
    success_url = reverse_lazy('newsletter:client_list')

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
    success_url = reverse_lazy('newsletter:client_list')

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
    context_object_name = 'mailings'

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
    success_url = reverse_lazy('newsletter:mailing_list')

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
    success_url = reverse_lazy('newsletter:mailing_list')

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
    success_url = reverse_lazy('newsletter:mailing_list')

    def get_queryset(self):
        return Mailing.objects.filter(owner=self.request.user)

    def test_func(self):
        mailing = self.get_object()
        return mailing.owner == self.request.user


class MessageListView(LoginRequiredMixin, ListView):
    """
    Представление для отображения списка сообщений текущего пользователя.
    """
    model = Message
    template_name = 'newsletter/message_list.html'
    context_object_name = 'messages'

    def get_queryset(self):
        return Message.objects.filter(owner=self.request.user)


class MessageDetailView(LoginRequiredMixin, DetailView):
    """
    Представление для отображения деталей сообщения текущего пользователя.
    """
    model = Message
    template_name = 'newsletter/message_detail.html'

    def get_queryset(self):
        return Message.objects.filter(owner=self.request.user)


class MessageCreateView(LoginRequiredMixin, CreateView):
    """
    Представление для создания нового сообщения.
    """
    model = Message
    form_class = MessageForm
    template_name = 'newsletter/message_form.html'
    success_url = reverse_lazy('newsletter:message_list')

    def form_valid(self, form):
        form.instance.owner = self.request.user
        return super().form_valid(form)


class MessageUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    """
    Представление для редактирования существующего сообщения.
    """
    model = Message
    form_class = MessageForm
    template_name = 'newsletter/message_form.html'
    success_url = reverse_lazy('newsletter:message_list')

    def get_queryset(self):
        return Message.objects.filter(owner=self.request.user)

    def test_func(self):
        message = self.get_object()
        return message.owner == self.request.user


class MessageDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    """
    Представление для удаления сообщения.
    """
    model = Message
    template_name = 'newsletter/message_confirm_delete.html'
    success_url = reverse_lazy('newsletter:message_list')

    def get_queryset(self):
        return Message.objects.filter(owner=self.request.user)

    def test_func(self):
        message = self.get_object()
        return message.owner == self.request.user


class ReportListView(LoginRequiredMixin, ListView):
    """
    Представление для простмотра отчётов по рассылке.
    """
    model = MailingAttempt
    template_name = 'newsletter/report_list.html'


class ReportDetailView(LoginRequiredMixin, DetailView):
    """
    Представление для детализации отчёта.
    """
    model = MailingAttempt
    template_name = 'newsletter/report_detail.html'


class HomePageView(TemplateView):
    template_name = 'newsletter/home.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['random_posts'] = BlogPost.objects.filter(is_published=True).order_by('?')[:3]
        return context
