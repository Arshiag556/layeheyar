# Generated by Django 5.0.7 on 2024-11-06 18:06

import django_jalali.db.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0012_rename_is_verifyed_useraccount_is_verified'),
    ]

    operations = [
        migrations.CreateModel(
            name='Bar',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('date', django_jalali.db.models.jDateField()),
            ],
        ),
    ]
