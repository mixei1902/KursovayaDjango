from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone

from .forms import ClientForm, MessageForm, MailingForm
from .models import Client, Message, Mailing
from .tasks import send_newsletters_for_mailing


def index(request):
    return HttpResponse("Hello, world. You're at the newsletter index.")


def client_list(request):
    """
    Представление для отображения списка клиентов текущего пользователя.
    """
    clients = Client.objects.filter(owner=request.user)
    return render(request, 'newsletter/client_list.html', {'clients': clients})


def client_detail(request, pk):
    """
    Представление для отображения деталей клиента текущего пользователя.
    """
    client = get_object_or_404(Client, pk=pk, owner=request.user)
    return render(request, 'newsletter/client_detail.html', {'client': client})


def client_create(request):
    """
    Представление для создания нового клиента.
    """
    if request.method == "POST":
        form = ClientForm(request.POST)
        if form.is_valid():
            client = form.save(commit=False)
            client.owner = request.user
            client.save()
            return redirect('client_list')
    else:
        form = ClientForm()
    return render(request, 'newsletter/client_form.html', {'form': form})


def client_update(request, pk):
    """
    Представление для редактирования существующего клиента.
    """
    client = get_object_or_404(Client, pk=pk, owner=request.user)
    if request.method == "POST":
        form = ClientForm(request.POST, instance=client)
        if form.is_valid():
            form.save()
            return redirect('client_list')
    else:
        form = ClientForm(instance=client)
    return render(request, 'newsletter/client_form.html', {'form': form})


def client_delete(request, pk):
    """
    Представление для удаления клиента.
    """
    client = get_object_or_404(Client, pk=pk, owner=request.user)
    if request.method == "POST":
        client.delete()
        return redirect('client_list')
    return render(request, 'newsletter/client_confirm_delete.html', {'client': client})


def message_list(request):
    """
    Представление для отображения списка сообщений текущего пользователя.
    """
    messages = Message.objects.filter(owner=request.user)
    return render(request, 'newsletter/message_list.html', {'messages': messages})


def message_detail(request, pk):
    """
    Представление для отображения деталей сообщения текущего пользователя.
    """
    message = get_object_or_404(Message, pk=pk, owner=request.user)
    return render(request, 'newsletter/message_detail.html', {'message': message})


def message_create(request):
    """
    Представление для создания нового сообщения.
    """
    if request.method == "POST":
        form = MessageForm(request.POST)
        if form.is_valid():
            message = form.save(commit=False)
            message.owner = request.user
            message.save()
            return redirect('message_list')
    else:
        form = MessageForm()
    return render(request, 'newsletter/message_form.html', {'form': form})


def message_update(request, pk):
    """
    Представление для редактирования существующего сообщения.
    """
    message = get_object_or_404(Message, pk=pk, owner=request.user)
    if request.method == "POST":
        form = MessageForm(request.POST, instance=message)
        if form.is_valid():
            form.save()
            return redirect('message_list')
    else:
        form = MessageForm(instance=message)
    return render(request, 'newsletter/message_form.html', {'form': form})


def message_delete(request, pk):
    """
    Представление для удаления сообщения.
    """
    message = get_object_or_404(Message, pk=pk, owner=request.user)
    if request.method == "POST":
        message.delete()
        return redirect('message_list')
    return render(request, 'newsletter/message_confirm_delete.html', {'message': message})


def mailing_list(request):
    """
    Представление для отображения списка рассылок текущего пользователя.
    """
    mailings = Mailing.objects.filter(owner=request.user)
    return render(request, 'newsletter/mailing_list.html', {'mailings': mailings})


def mailing_detail(request, pk):
    """
    Представление для отображения деталей рассылки текущего пользователя.
    """
    mailing = get_object_or_404(Mailing, pk=pk, owner=request.user)
    return render(request, 'newsletter/mailing_detail.html', {'mailing': mailing})


def mailing_create(request):
    """
    Представление для создания новой рассылки.
    """
    if request.method == "POST":
        form = MailingForm(request.POST)
        if form.is_valid():
            mailing = form.save(commit=False)
            mailing.owner = request.user
            mailing.save()
            form.save_m2m()

            if mailing.start_date <= timezone.now():
                send_newsletters_for_mailing(mailing)

            return redirect('mailing_list')
    else:
        form = MailingForm()
    return render(request, 'newsletter/mailing_form.html', {'form': form})


def mailing_update(request, pk):
    """
    Представление для редактирования существующей рассылки.
    """
    mailing = get_object_or_404(Mailing, pk=pk, owner=request.user)
    if request.method == "POST":
        form = MailingForm(request.POST, instance=mailing)
        if form.is_valid():
            form.save()
            return redirect('mailing_list')
    else:
        form = MailingForm(instance=mailing)
    return render(request, 'newsletter/mailing_form.html', {'form': form})


def mailing_delete(request, pk):
    """
    Представление для удаления рассылки.
    """
    mailing = get_object_or_404(Mailing, pk=pk, owner=request.user)
    if request.method == "POST":
        mailing.delete()
        return redirect('mailing_list')
    return render(request, 'newsletter/mailing_confirm_delete.html', {'mailing': mailing})
