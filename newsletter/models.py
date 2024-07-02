from django.db import models
from django.utils import timezone


class Client(models.Model):
    email = models.EmailField(unique=True)
    full_name = models.CharField(max_length=255)
    comment = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.full_name


class Message(models.Model):
    subject = models.CharField(max_length=255)
    body = models.TextField()

    def __str__(self):
        return self.subject


class Mailing(models.Model):
    STATUS_CHOICES = [
        ('created', 'Created'),
        ('running', 'Running'),
        ('completed', 'Completed'),
    ]

    start_date = models.DateTimeField()
    periodicity = models.CharField(max_length=50, choices=[
        ('daily', 'Daily'),
        ('weekly', 'Weekly'),
        ('monthly', 'Monthly')
    ])
    status = models.CharField(max_length=50, choices=STATUS_CHOICES, default='created')
    message = models.OneToOneField(Message, on_delete=models.CASCADE)
    clients = models.ManyToManyField(Client)

    def __str__(self):
        return f"Mailing {self.id} - {self.status}"


class MailingAttempt(models.Model):
    STATUS_CHOICES = [
        ('success', 'Success'),
        ('failed', 'Failed'),
    ]

    mailing = models.ForeignKey(Mailing, on_delete=models.CASCADE)
    attempt_date = models.DateTimeField(default=timezone.now)
    status = models.CharField(max_length=50, choices=STATUS_CHOICES)
    server_response = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"Attempt for Mailing {self.mailing.id} on {self.attempt_date}"
