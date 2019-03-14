from django.contrib.gis.db import models


class Restaurant(models.Model):

    id = models.CharField(max_length=36, primary_key=True)
    rating = models.PositiveSmallIntegerField()
    name = models.CharField(max_length=100)
    site = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=100)
    street = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    location = models.PointField(null=True, spatial_index=True, srid=4326, geography=True)


