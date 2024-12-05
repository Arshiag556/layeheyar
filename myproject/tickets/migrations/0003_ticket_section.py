# Generated by Django 5.0.7 on 2024-11-21 10:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tickets', '0002_ticketresponse_attachment'),
    ]

    operations = [
        migrations.AddField(
            model_name='ticket',
            name='section',
            field=models.CharField(choices=[('technical', 'بخش فنی'), ('support', 'بخش پشتیبانی'), ('sales', 'بخش فروش'), ('other', 'سایر بخش\u200cها')], default='other', max_length=100),
        ),
    ]
