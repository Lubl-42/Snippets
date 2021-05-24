from django.db import models
import  datetime
from django.contrib.auth.models import User

class Snippet(models.Model):
    name = models.CharField(max_length=100)
    lang = models.CharField(max_length=30)
    code = models.TextField(max_length=5000)
    creation_date = models.DateTimeField(default=datetime.datetime.now())
    visible=models.BooleanField(default=True, null=False)
    user = models.ForeignKey(to=User, on_delete=models.CASCADE,
                             blank=True, null=True)

class Comment(models.Model):
    text=models.TextField(max_length=1000)
    creation_date= models.DateTimeField(default=datetime.datetime.now())
    author= models.ForeignKey(to=User, on_delete=models.CASCADE, blank=True, null=True )
    snippet=models.ForeignKey(to=Snippet, on_delete=models.CASCADE, blank=True, null=True)

class Account (models.Model):
    user = models.ForeignKey(to=User, on_delete=models.CASCADE,
                             blank=True, null=True)
    amount = models.IntegerField()
    comment = models.CharField(max_length=500, default='Начисление без комментариев, автоматическое')
    creation_date = models.DateTimeField(default=datetime.datetime.now())

    def __add__ (self,other):
        return self.amount+other.amount

class Elektro (models.Model):
    user = models.ForeignKey(to=User, on_delete=models.CASCADE,
                             blank=True, null=True)
    account=models.ForeignKey(to=Account, on_delete=models.CASCADE,
                             blank=True, null=True)
    el_acc = models.FloatField()
    creation_date = models.DateTimeField(default=datetime.datetime.now())
    comment = models.CharField(max_length=500, default='No comment')


class Tarif (models.Model):
    tarif = models.FloatField()
    creation_date = models.DateTimeField(default=datetime.datetime.now())
    comment = models.CharField(max_length=500, default='No comment' )
