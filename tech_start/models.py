from django.db import models


class Location(models.Model):
    address = models.CharField(max_length=200)
    city = models.CharField(max_length=70)
    country = models.CharField(max_length=70)
    opening_hours = models.TimeField(default='00:00') #These default hours in case if the branch is open 24 hours a day
    closing_hours = models.TimeField(default='23:59')

    def __str__(self) -> str:
        return f"{self.address}, {self.city}, {self.country}, Work time: {self.opening_hours}-{self.closing_hours}"


class Establishment(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(null=True, blank=True)
    location = models.ForeignKey(Location, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return f"{self.id}: {self.name} in {self.location.address}, {self.location.city}"


class Product(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(null=True, blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    quantity = models.PositiveIntegerField()
    establishment = models.ForeignKey(Establishment, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return f"Product: {self.name}, establishment: {self.establishment.name}, {self.establishment.location.address}"
