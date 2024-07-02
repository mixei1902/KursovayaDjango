from apscheduler.schedulers.background import BackgroundScheduler
from django.utils import timezone
from django_apscheduler.jobstores import DjangoJobStore, register_events, register_job

from .models import Mailing
from .tasks import send_newsletters_for_mailing


def start_scheduler():
    """
    Функция для запуска планировщика задач.
    """
    scheduler = BackgroundScheduler()
    scheduler.add_jobstore(DjangoJobStore(), "default")

    @register_job(scheduler, "interval", minutes=1)
    def timed_job():
        """
        Периодическая задача для отправки сообщений по расписанию.
        """
        now = timezone.now()
        mailings = Mailing.objects.filter(start_date__lte=now, status='created')
        for mailing in mailings:
            send_newsletters_for_mailing(mailing)

    register_events(scheduler)
    scheduler.start()

    print("Запуск рассылки...")
