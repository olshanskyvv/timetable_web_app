from django.contrib.auth.models import AbstractUser
from django.db import models
from django.urls import reverse


class User(AbstractUser):
    group = models.CharField(max_length=10, verbose_name='Номер группы')
    is_elder = models.BooleanField(verbose_name='Стороста', default=False)


class Timetable(models.Model):
    group = models.CharField(max_length=10, verbose_name='Номер группы')
    week1 = models.OneToOneField('Week', on_delete=models.CASCADE, related_name='timetable1', verbose_name='Первая неделя')
    week2 = models.OneToOneField('Week', on_delete=models.CASCADE, related_name='timetable2', verbose_name='Вторая неделя')

    def __str__(self):
        return self.group


class Week(models.Model):
    number = models.IntegerField(verbose_name='Номер недели')

    def __str__(self):
        return 'Неделя ' + str(self.number)


class Day(models.Model):
    week = models.ForeignKey('Week', on_delete=models.CASCADE, verbose_name='Неделя')
    name = models.CharField(max_length=20, verbose_name='День недели')

    def __str__(self):
        return self.name


class Lesson(models.Model):
    day = models.ForeignKey('Day', on_delete=models.CASCADE, verbose_name='День')
    number = models.CharField(max_length=10, verbose_name='Номер пары')
    time = models.CharField(max_length=20, verbose_name='Время пары')
    type = models.CharField(max_length=25, verbose_name='Тип пары')
    name = models.CharField(max_length=100, verbose_name='Название курса')
    note = models.TextField(verbose_name='Заметки', default='')

    def __str__(self):
        return self.name

    def get_absolut_url(self):
        return reverse('lesson', kwargs={'lesson_id': self.pk})


class Info(models.Model):
    lesson = models.ForeignKey('Lesson', on_delete=models.CASCADE, verbose_name='Пара')
    content = models.CharField(max_length=255, verbose_name='Информация')

    def __str__(self):
        return self.content
