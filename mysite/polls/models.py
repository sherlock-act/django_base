from django.db import models
import datetime


# Create your models here.
from django.utils import timezone


class Question(models.Model):
    """问题模型类"""
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('datepublished')

    def was_published_recently(self):
        now = timezone.now()

        return now-datetime.timedelta(days=1)<=self.pub_date<=now

    def __str__(self):
        return self.question_text


class Choice(models.Model):
    """选项模型类"""
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

    def __str__(self):
        return self.choice_text
