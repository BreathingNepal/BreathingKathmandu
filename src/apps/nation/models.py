from django.db import models
from django.db.models import Manager as GeoManager
from django.contrib.gis.db import models as gis_models


class Instance(models.Model):
    name = models.CharField(max_length=50)
    location = gis_models.PointField(srid=4326)
    objects = GeoManager()


class Nepal(models.Model):
    dist_id = models.IntegerField()
    district = models.CharField(max_length=18)
    zone_name = models.CharField(max_length=16)
    region = models.CharField(max_length=16)
    diss = models.IntegerField()
    xc = models.FloatField()
    yc = models.FloatField()
    geom = gis_models.MultiPolygonField(srid=4326)

    def __str__(self):
        return self.district


class InstanceConservation(models.Model):
    name = models.CharField(max_length=50)
    location = gis_models.PointField(srid=4326)
    objects = GeoManager()


class Conservation(models.Model):
    fid_protec = models.BigIntegerField()
    name = models.CharField(max_length=50)
    type = models.CharField(max_length=25)
    area = models.IntegerField()
    descriptio = models.CharField(max_length=254)
    sources = models.CharField(max_length=254)
    issues = models.CharField(max_length=254)
    remarks = models.CharField(max_length=254)
    quality = models.CharField(max_length=254)
    qltyremark = models.CharField(max_length=254)
    date_time = models.CharField(max_length=254)
    shape_leng = models.FloatField()
    shape_area = models.FloatField()
    geom = gis_models.MultiPolygonField(srid=4326)

    def __str__(self):
        return self.name
