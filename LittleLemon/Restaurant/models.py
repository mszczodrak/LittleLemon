from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator


# Create your models here.

class Booking(models.Model):
    name = models.CharField(max_length=255)
    no_of_guests = models.SmallIntegerField(validators=[
        MaxValueValidator(6),
        MaxValueValidator(1)
    ])
    booking_data = models.DateTimeField()

class Menu(models.Model):
    title = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    inventory = models.SmallIntegerField(validators=[
        MaxValueValidator(5),
        MaxValueValidator(0)
    ])

    def __str__(self):
        return f'{self.title} : {str(self.price)}'


class MenuItem(models.Model):
    title = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    inventory = models.SmallIntegerField()

    def get_item(self):
        return f'{self.title} : {str(self.price)}'