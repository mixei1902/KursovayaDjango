import logging
import smtplib
from django.conf import settings
from django.core.mail import send_mail
from django.utils import timezone
from apscheduler.schedulers.blocking import BlockingScheduler
from apscheduler.triggers.cron import CronTrigger
from django_apscheduler.jobstores import DjangoJobStore
from django_apscheduler.models import DjangoJobExecution

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
            status = 'Ошибка'
            logger.error(f"Ошибка отправки на почту {client.email}: {e}")

        MailingAttempt.objects.create(
            mailing=mailing,
            attempt_date=timezone.now(),
            status=status,
            server_response=server_response,
        )

    mailing.status = 'Завершена'
    mailing.save()


def delete_old_job_executions(max_age=604_800):
    """ This job deletes all apscheduler job executions older than `max_age` from the database. """
    DjangoJobExecution.objects.delete_old_job_executions(max_age)


def start_scheduler():
    scheduler = BlockingScheduler(timezone=settings.TIME_ZONE)
    scheduler.add_jobstore(DjangoJobStore(), "default")

    scheduler.add_job(
        send_newsletters,
        trigger=CronTrigger(minute='*/1'),
        id="send_newsletters",
        max_instances=1,
        replace_existing=True,
    )
    logger.info("Добавлена работа 'send_newsletters'.")

    scheduler.add_job(
        delete_old_job_executions,
        trigger=CronTrigger(
            day_of_week="mon", hour="00", minute="00"
        ),
        id="delete_old_job_executions",
        max_instances=1,
        replace_existing=True,
    )
    logger.info("Добавлена работа 'delete_old_job_executions'.")

    try:
        logger.info("Запуск планировщика...")
        scheduler.start()
    except KeyboardInterrupt:
        logger.info("Остановка планировщика...")
        scheduler.shutdown()
    logger.info("Планировщик остановлен.")
