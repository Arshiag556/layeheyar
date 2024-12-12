from django.db import models
from django.conf import settings
from myapp.models import UserAccount

class Ticket(models.Model):
    STATUS_CHOICES = [
        ('open', 'در انتظار پاسخ'),
        ('answered', 'باسخ داده شد'),
        ('closed', 'بسته شده'),
    ]
    section = models.CharField(max_length=100, choices=[
        ('technical', 'بخش فنی'),
        ('support', 'بخش پشتیبانی'),
        ('sales', 'بخش فروش'),
        ('other', 'سایر بخش‌ها'),
    ], default='other')

    user = models.ForeignKey(UserAccount, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    description = models.TextField()
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='open')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

class TicketResponse(models.Model):
    ticket = models.ForeignKey(Ticket, on_delete=models.CASCADE, related_name='responses')
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    message = models.TextField()
    attachment = models.FileField(upload_to='attachments/', blank=True, null=True)  # فیلد پیوست
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Response by {self.user.name} on {self.ticket.title}'
