from django.db import models
from datetime import datetime



class Boss(models.Model):
    name = models.CharField("Your Name ",max_length=150)

    def __str__(self):
        return self.name


class Employee(models.Model):
    full_name = models.CharField("Full Name ", max_length=150)
    position = models.CharField("Position ", null=True, blank=True, max_length=150)
    date_hire = models.DateField(default=datetime.now(), blank=True)
    salary = models.IntegerField("Amount of wages ", default=0)
    boss = models.ForeignKey(Boss, on_delete=models.CASCADE, null=True)


    def __str__(self):
        return self.full_name



