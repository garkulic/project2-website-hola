 # Generated by Django 4.1.7 on 2023-04-22 18:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0004_lessons_date_lessons_rang_alter_lessons_lesson_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='lessons',
            name='date',
        ),
        migrations.RemoveField(
            model_name='lessons',
            name='rang',
        ),
    ]
