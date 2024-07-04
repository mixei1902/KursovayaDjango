from django.core.management.base import BaseCommand

from ...tasks import send_newsletters


class Command(BaseCommand):
    help = 'Отправить все рассылки'

    def handle(self, *args, **kwargs):
        send_newsletters()
        self.stdout.write(self.style.SUCCESS('Успешная отправка'))
