from django.conf import settings
from django.db import models
from django.utils import timezone


class Client(models.Model):
    """
    Модель для представления клиента сервиса.
    Содержит информацию о контактном email, ФИО, комментарии и владельце.
    """
    email = models.EmailField(unique=True)
    full_name = models.CharField(max_length=255)
    comment = models.TextField(blank=True, null=True)
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

    def __str__(self):
        return self.full_name

    class Meta:
        verbose_name = "Клиент"
        verbose_name_plural = "Клиенты"


class Message(models.Model):
    """
    Модель для представления сообщения рассылки.
    Содержит тему и тело сообщения, а также владельца.
    """
    subject = models.CharField(max_length=255)
    body = models.TextField()
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

    def __str__(self):
        return self.subject

    class Meta:
        verbose_name = "Сообщение"
        verbose_name_plural = "Сообщения"

class Mailing(models.Model):
    """
    Модель для представления рассылки.
    Содержит информацию о дате начала, периодичности, статусе, сообщении, клиентах и владельце.
    """
    STATUS_CHOICES = [
        ('created', 'Создана'),
        ('running', 'Запущена'),
        ('completed', 'Завершена'),
    ]

    start_date = models.DateTimeField()
    periodicity = models.CharField(max_length=50, choices=[
        ('daily', 'Раз в день'),
        ('weekly', 'Раз в неделю'),
        ('monthly', 'Раз в месяц')
    ])
    status = models.CharField(max_length=50, choices=STATUS_CHOICES, default='created')
    message = models.OneToOneField(Message, on_delete=models.CASCADE)
    clients = models.ManyToManyField(Client)
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    def __str__(self):
        return f"Рассылка {self.id} - {self.status}"


class MailingAttempt(models.Model):
    """
    Модель для представления попытки рассылки.
    Содержит информацию о рассылке, дате попытки, статусе и ответе почтового сервера.
    """
    STATUS_CHOICES = [
        ('success', 'Успешна'),
        ('failed', 'Провалена'),
    ]

    mailing = models.ForeignKey(Mailing, on_delete=models.CASCADE)
    attempt_date = models.DateTimeField(default=timezone.now)
    status = models.CharField(max_length=50, choices=STATUS_CHOICES)
    server_response = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"Попытка рассылки {self.mailing.id} на {self.attempt_date}"
