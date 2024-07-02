from apscheduler.schedulers.background import BackgroundScheduler
from django_apscheduler.jobstores import DjangoJobStore, register_events, register_job

from .tasks import send_newsletters

scheduler = BackgroundScheduler()
scheduler.add_jobstore(DjangoJobStore(), "default")


@register_job(scheduler, "interval", minutes=1)
def timed_job():
    send_newsletters()


register_events(scheduler)

scheduler.start()
