from django.db import models


class Boat(models.Model):
    price = models.IntegerField()
    capacity = models.IntegerField()
    name = models.CharField(max_length=200)
    image = models.CharField(max_length=200)
    description = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class Booking(models.Model):
    end_date = models.DateField()
    price = models.IntegerField()
    start_date = models.DateField()
    user = models.CharField(max_length=200)
    boat = models.ForeignKey(Boat, on_delete=models.CASCADE)

    def __str__(self):
        return self.user
