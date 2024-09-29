# main/models.py
from django.db import models

class City(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Country(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class State(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Subscription(models.Model):
    plan_name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=6, decimal_places=2)

    def __str__(self):
        return self.plan_name

class WorkoutCategory(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Index(models.Model):
        name = models.CharField(max_length=100)

        def __str__(self):
            return self.name


class Payment(models.Model):
        name = models.CharField(max_length=100)

        def __str__(self):
            return self.name
class Users(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name
