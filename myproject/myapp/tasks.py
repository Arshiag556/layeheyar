# tasks.py (در صورت استفاده از Celery)
from celery import shared_task
from datetime import timedelta
from django.utils import timezone
from .models import Notification

@shared_task
def deactivate_old_notifications():
    expiration_date = timezone.now() - timedelta(days=1)  # 7 روز
    Notification.objects.filter(created_at__lt=expiration_date).update(is_active=False)
