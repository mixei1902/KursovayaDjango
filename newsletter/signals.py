# newsletter/signals.py

from django.db.models.signals import post_migrate
from django.dispatch import receiver
from newsletter.scheduler import start_scheduler

@receiver(post_migrate)
def start_scheduler_after_migrations(sender, **kwargs):
    start_scheduler()
