from django.shortcuts import render, get_object_or_404, redirect
from .forms import MailingForm
from .models import Mailing


def mailing_list(request):
    mailings = Mailing.objects.all()
    return render(request, 'newsletter/mailing_list.html', {'mailings': mailings})


def mailing_detail(request, pk):
    mailing = get_object_or_404(Mailing, pk=pk)
    return render(request, 'newsletter/mailing_detail.html', {'mailing': mailing})


def mailing_create(request):
    if request.method == "POST":
        form = MailingForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('mailing_list')
    else:
        form = MailingForm()
    return render(request, 'newsletter/mailing_form.html', {'form': form})


def mailing_update(request, pk):
    mailing = get_object_or_404(Mailing, pk=pk)
    if request.method == "POST":
        form = MailingForm(request.POST, instance=mailing)
        if form.is_valid():
            form.save()
            return redirect('mailing_list')
    else:
        form = MailingForm(instance=mailing)
    return render(request, 'newsletter/mailing_form.html', {'form': form})


def mailing_delete(request, pk):
    mailing = get_object_or_404(Mailing, pk=pk)
    if request.method == "POST":
        mailing.delete()
        return redirect('mailing_list')
    return render(request, 'newsletter/mailing_confirm_delete.html', {'mailing': mailing})
