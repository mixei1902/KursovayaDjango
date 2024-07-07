from django.core.management.base import BaseCommand

from newsletter.scheduler import start_scheduler


class Command(BaseCommand):
    help = 'Запустить планировщик для рассылок'

    def handle(self, *args, **kwargs):
        start_scheduler()
