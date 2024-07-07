from apscheduler.executors.pool import ThreadPoolExecutor, ProcessPoolExecutor
from apscheduler.schedulers.background import BackgroundScheduler
from apscheduler.triggers.interval import IntervalTrigger
from django_apscheduler.jobstores import DjangoJobStore, register_events

from newsletter.tasks import send_newsletters


def start_scheduler():
    """
    Функция для запуска планировщика задач.
    """
    executors = {
        'default': ThreadPoolExecutor(20),
        'processpool': ProcessPoolExecutor(5)
    }

    job_defaults = {
        'coalesce': False,
        'max_instances': 3,
    }

    scheduler = BackgroundScheduler(executors=executors, job_defaults=job_defaults)
    scheduler.add_jobstore(DjangoJobStore(), "default")

    scheduler.add_job(
        send_newsletters,
        trigger=IntervalTrigger(minutes=1),
        id='send_newsletters',
        replace_existing=True,
    )

    register_events(scheduler)
    scheduler.start()

    print("Рассылка запущена...")
