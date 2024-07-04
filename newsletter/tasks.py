import logging
import smtplib

from django.conf import settings
from django.core.mail import send_mail
from django.utils import timezone

from .models import Mailing, MailingAttempt

logger = logging.getLogger(__name__)


def send_newsletters():
    """
    Функция для отправки сообщений для всех активных рассылок.
    """
    mailings = Mailing.objects.filter(status='created')
    for mailing in mailings:
        send_newsletters_for_mailing(mailing)


def send_newsletters_for_mailing(mailing):
    """
    Функция для отправки сообщений для конкретной рассылки.
    """
    clients = mailing.clients.all()
    for client in clients:
        try:
            server_response = send_mail(
                mailing.message.subject,
                mailing.message.body,
                settings.DEFAULT_FROM_EMAIL,
                [client.email],
                fail_silently=False,
            )
            status = 'Успешно'
        except smtplib.SMTPException as e:
            server_response = str(e)
            status = 'failed'
            logger.error(f"Ошибка отправки на почту {client.email}: {e}")

        MailingAttempt.objects.create(
            mailing=mailing,
            attempt_date=timezone.now(),
            status=status,
            server_response=server_response,
        )

    mailing.status = 'Завершена'
    mailing.save()


def timed_job():
    """
    Периодическая задача для отправки сообщений по расписанию.
    """
    now = timezone.now()
    mailings = Mailing.objects.filter(start_date__lte=now, status='created')
    for mailing in mailings:
        send_newsletters_for_mailing(mailing)
