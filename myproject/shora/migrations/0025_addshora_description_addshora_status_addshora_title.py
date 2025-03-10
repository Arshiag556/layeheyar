# Generated by Django 5.0.7 on 2024-11-10 11:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shora', '0024_rename_paymentreceipt_addshora'),
    ]

    operations = [
        migrations.AddField(
            model_name='addshora',
            name='description',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='addshora',
            name='status',
            field=models.CharField(choices=[('draft', 'Draft'), ('approved', 'Approved'), ('rejected', 'Rejected')], default='draft', max_length=10),
        ),
        migrations.AddField(
            model_name='addshora',
            name='title',
            field=models.CharField(max_length=200, null=True),
        ),
    ]
