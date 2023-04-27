from django.db import models


# Create your models here.
class Word(models.Model):
    word = models.CharField('Слово', max_length=25)
    translate = models.CharField('Перевод', max_length=50)

    def __str__(self):
        return self.word

    class Meta:
        verbose_name = 'Слово'
        verbose_name_plural = 'Слова'

class News(models.Model):
    title = models.CharField('Заголовок', max_length=50)
    content = models.TextField('Содержание')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Новость'
        verbose_name_plural = 'Новости'

class Lessons(models.Model):
    name = models.CharField('Урок', max_length=50)
    date = models.DateField('Дата')
    lesson = models.TextField('Тема')
    rang = models.IntegerField('Сложность', default=1)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Урок'
        verbose_name_plural = 'Уроки'