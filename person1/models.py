from django.db import models

class Person(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=255)
    sec=models.CharField(max_length=255)
   

