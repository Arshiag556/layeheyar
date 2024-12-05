# Generated by Django 5.0.7 on 2024-11-10 15:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shora', '0029_alter_document_subject'),
    ]

    operations = [
        migrations.AlterField(
            model_name='document',
            name='subject',
            field=models.CharField(choices=[('Chois', 'انتحاب'), ('economic', 'اقتصادی'), ('social', 'اجتماعی'), ('Cultural', 'فرهنگی و آموزشی'), ('legal', 'حقوقی'), ('other', 'سایر')], default='Chois', max_length=10),
        ),
    ]
