# Generated by Django 4.1.7 on 2023-04-24 08:12

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0005_remove_lessons_date_remove_lessons_rang'),
    ]

    operations = [
        migrations.AddField(
            model_name='lessons',
            name='data',
            field=models.TimeField(default=django.utils.timezone.now, verbose_name='Дата'),
            preserve_default=False,
        ),
    ]