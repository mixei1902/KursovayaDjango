from django.conf import settings
from django.core.mail import send_mail

from .models import Mailing


def send_newsletters():
    mailings = Mailing.objects.all()
    for mailing in mailings:
        send_mail(
            mailing.subject,
            mailing.body,
            settings.DEFAULT_FROM_EMAIL,
            ['mixei1902@yandex.ru'],
            fail_silently=False,
        )
