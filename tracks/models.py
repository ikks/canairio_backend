from django.contrib.gis.db import models
from django.contrib.postgres.fields import JSONField
from django.contrib.auth.models import User


class Track(models.Model):

    id = models.CharField(max_length=50, primary_key=True)
    name = models.CharField(max_length=100)
    device = models.CharField(max_length=100)
    date = models.CharField(max_length=100)
    user = models.ForeignKey(User, related_name='tracks', on_delete=models.SET_NULL, null=True)

class TrackPoint(models.Model):
    geom = models.PointField()
    track_name = models.CharField(max_length=128, null=True)
    device_id = models.CharField(max_length=128)
    pm25 = models.DecimalField(max_digits=19, decimal_places=6)
    pm10 = models.DecimalField(max_digits=19, decimal_places=6, null=True)
    humidity = models.DecimalField(max_digits=19, decimal_places=6, null=True)
    spd = models.DecimalField(max_digits=19, decimal_places=6, null=True)
    altitude = models.DecimalField(max_digits=19, decimal_places=6, null=True)
    sampled_at = models.DateTimeField()
    created_at = models.DateTimeField(auto_now_add=True, primary_key=True)
    attributes = JSONField(default=dict)
