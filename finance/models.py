from django.db import models
from django.urls import reverse

# Create your models here.
class Cash(models.Model):
    title = models.CharField(max_length=30)
    Cash = models.IntegerField()
    id = models.IntegerField(primary_key=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('home')



class Check(models.Model):
    title = models.CharField(max_length=30)
    Check = models.IntegerField()
    Account_number = models.CharField(max_length=14)
    id = models.IntegerField(primary_key=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('home')
