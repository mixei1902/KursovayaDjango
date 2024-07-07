from django.core.management.base import BaseCommand

from ...scheduler import start_scheduler


class Command(BaseCommand):
    help = 'Отправить все рассылки'

    def handle(self, *args, **kwargs):
        start_scheduler()
