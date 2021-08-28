from django.db import models


# Create your models here.
class BookInfo(models.Model):
    """书本类"""
    name = models.CharField(max_length=20)

    def __str__(self):
        """
        重写str方法修改类返回信息
        """
        return self.name


class PeopleInfo(models.Model):
    """人物类"""
    name = models.CharField(max_length=10)
    gender = models.BooleanField()
    book = models.ForeignKey(BookInfo, on_delete=models.CASCADE)

    def __str__(self):
        """
        重写str方法修改类返回信息
        """
        return self.name
