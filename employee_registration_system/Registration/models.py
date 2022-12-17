from django.db import models

# Create your models here.
class Position(models.Model):
    title=models.CharField(max_length=25)
class Employee(models.Model):
    name=models.CharField(max_length=100)
    mobileno=models.CharField(max_length=10)
    address=models.CharField(max_length=100)
    position=models.ForeignKey(Position, on_delete=models.CASCADE)