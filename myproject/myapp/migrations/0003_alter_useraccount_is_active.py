# Generated by Django 5.0.7 on 2024-09-11 15:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0002_alter_useraccount_is_active_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='useraccount',
            name='is_active',
            field=models.BooleanField(default=False),
        ),
    ]
