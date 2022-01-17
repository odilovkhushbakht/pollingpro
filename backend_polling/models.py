import datetime

from django.db import models
from datetime import date
from django.contrib.auth.models import User


class Polling(models.Model):
    name = models.CharField(max_length=200)
    start_date = models.DateField(auto_created=date.today())
    finished_date = models.DateField()
    description = models.TextField(max_length=1000, blank=True)
    status = models.BooleanField(default=True, blank=True)
    number = models.IntegerField(unique=True, editable=True)

    def __str__(self):
        return self.name


# 1 ответ текстом
# 2 ответ с выбором одного варианта
# 3 ответ с выбором нескольких вариантов
class Question(models.Model):
    text = models.TextField()
    style = models.IntegerField(default=1, blank=True)
    answer_multi_1 = models.CharField(max_length=200, blank=True, default='')
    answer_multi_2 = models.CharField(max_length=200, blank=True, default='')
    answer_multi_3 = models.CharField(max_length=200, blank=True, default='')
    answer_multi_4 = models.CharField(max_length=200, blank=True, default='')
    # answer_text = models.TextField(blank=True, default='')
    parent = models.ForeignKey(Polling, related_name='pol', to_field='number', on_delete=models.DO_NOTHING,
                               null=True, blank=True)


class UserCustom(models.Model):
    first_name = models.CharField(max_length=25, blank=True)
    last_name = models.CharField(max_length=25, blank=True)


class Participant(models.Model):
    user_data = models.ForeignKey(UserCustom, related_name='answer', on_delete=models.DO_NOTHING, blank=True, null=True)
    polling = models.CharField(max_length=200, default='')
    text = models.TextField(max_length=1000)
    answer_multi_1 = models.CharField(max_length=200, blank=True, default='')
    answer_multi_2 = models.CharField(max_length=200, blank=True, default='')
    answer_multi_3 = models.CharField(max_length=200, blank=True, default='')
    answer_multi_4 = models.CharField(max_length=200, blank=True, default='')
    answer_text = models.TextField(max_length=2000, blank=True, default='')
    date = models.DateField(blank=True, default=datetime.date.today())
