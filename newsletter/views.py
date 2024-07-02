from django.shortcuts import render, get_object_or_404, redirect

from .forms import ClientForm, MessageForm, MailingForm
from .models import Client, Message, Mailing


# Clients CRUD
def client_list(request):
    clients = Client.objects.all()
    return render(request, 'newsletter/client_list.html', {'clients': clients})


def client_detail(request, pk):
    client = get_object_or_404(Client, pk=pk)
    return render(request, 'newsletter/client_detail.html', {'client': client})


def client_create(request):
    if request.method == "POST":
        form = ClientForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('client_list')
    else:
        form = ClientForm()
    return render(request, 'newsletter/client_form.html', {'form': form})


def client_update(request, pk):
    client = get_object_or_404(Client, pk=pk)
    if request.method == "POST":
        form = ClientForm(request.POST, instance=client)
        if form.is_valid():
            form.save()
            return redirect('client_list')
    else:
        form = ClientForm(instance=client)
    return render(request, 'newsletter/client_form.html', {'form': form})


def client_delete(request, pk):
    client = get_object_or_404(Client, pk=pk)
    if request.method == "POST":
        client.delete()
        return redirect('client_list')
    return render(request, 'newsletter/client_confirm_delete.html', {'client': client})


# Messages CRUD
def message_list(request):
    messages = Message.objects.all()
    return render(request, 'newsletter/message_list.html', {'messages': messages})


def message_detail(request, pk):
    message = get_object_or_404(Message, pk=pk)
    return render(request, 'newsletter/message_detail.html', {'message': message})


def message_create(request):
    if request.method == "POST":
        form = MessageForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('message_list')
    else:
        form = MessageForm()
    return render(request, 'newsletter/message_form.html', {'form': form})


def message_update(request, pk):
    message = get_object_or_404(Message, pk=pk)
    if request.method == "POST":
        form = MessageForm(request.POST, instance=message)
        if form.is_valid():
            form.save()
            return redirect('message_list')
    else:
        form = MessageForm(instance=message)
    return render(request, 'newsletter/message_form.html', {'form': form})


def message_delete(request, pk):
    message = get_object_or_404(Message, pk=pk)
    if request.method == "POST":
        message.delete()
        return redirect('message_list')
    return render(request, 'newsletter/message_confirm_delete.html', {'message': message})


# Mailings CRUD
def mailing_list(request):
    mailings = Mailing.objects.all()
    return render(request, 'newsletter/client_list.html', {'mailings': mailings})


def mailing_detail(request, pk):
    mailing = get_object_or_404(Mailing, pk=pk)
    return render(request, 'newsletter/client_detail.html', {'mailing': mailing})


def mailing_create(request):
    if request.method == "POST":
        form = MailingForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('mailing_list')
    else:
        form = MailingForm()
    return render(request, 'newsletter/client_form.html', {'form': form})


def mailing_update(request, pk):
    mailing = get_object_or_404(Mailing, pk=pk)
    if request.method == "POST":
        form = MailingForm(request.POST, instance=mailing)
        if form.is_valid():
            form.save()
            return redirect('mailing_list')
    else:
        form = MailingForm(instance=mailing)
    return render(request, 'newsletter/client_form.html', {'form': form})


def mailing_delete(request, pk):
    mailing = get_object_or_404(Mailing, pk=pk)
    if request.method == "POST":
        mailing.delete()
        return redirect('mailing_list')
    return render(request, 'newsletter/client_confirm_delete.html', {'mailing': mailing})
