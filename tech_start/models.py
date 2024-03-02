from django.db import models

class Product(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(null=True, blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    quantity = models.PositiveIntegerField()

    def __str__(self) -> str:
        return f"Product: {self.name}, price: {self.price}, quantity: {self.quantity}"


class Location(models.Model):
    address = models.CharField(max_length=200)
    city = models.CharField(max_length=70)
    country = models.CharField(max_length=70)
    opening_hours = models.TimeField(null=True)


class Establishment(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(null=True, blank=True)
    location = models.ForeignKey(Location, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return self.name



