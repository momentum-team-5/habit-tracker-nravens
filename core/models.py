from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    pass

class Habit(models.Model):
    subject = models.CharField(max_length=255)
    action = models.CharField(max_length=255)
    amount = models.IntegerField()
    user = models.ForeignKey('User', related_name = 'habits', on_delete=models.CASCADE)
    date = models.DateField(auto_now=True)

class Record(models.Model):
    date = models.DateField(auto_now=True)
    amount = models.IntegerField()
    habit = models.ForeignKey('Habit', related_name = 'records', on_delete=models.CASCADE)
    
    class Meta:
        constraints = [ models.UniqueConstraint(fields=['habit', 'date'], name='unique_habit') ]