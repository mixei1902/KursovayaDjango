from django.contrib import admin
from .models import Mailing


@admin.register(Mailing)
class MailingAdmin(admin.ModelAdmin):
    list_display = ('subject', 'created_at', 'updated_at')
