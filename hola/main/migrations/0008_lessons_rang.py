# Generated by Django 4.1.7 on 2023-04-24 08:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0007_remove_lessons_data_lessons_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='lessons',
            name='rang',
            field=models.IntegerField(default=1, verbose_name='Сложность'),
        ),
    ]
