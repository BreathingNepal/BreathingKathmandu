# Generated by Django 2.1 on 2018-08-24 15:05

import django.contrib.gis.db.models.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('nation', '0003_instanceconservation'),
    ]

    operations = [
        migrations.CreateModel(
            name='Conservation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fid_protec', models.BigIntegerField()),
                ('name', models.CharField(max_length=50)),
                ('typ_e', models.CharField(max_length=25)),
                ('area', models.IntegerField()),
                ('descriptio', models.CharField(max_length=254)),
                ('sources', models.CharField(max_length=254)),
                ('issues', models.CharField(max_length=254)),
                ('remarks', models.CharField(max_length=254)),
                ('quality', models.CharField(max_length=254)),
                ('qltyremark', models.CharField(max_length=254)),
                ('date_time', models.CharField(max_length=254)),
                ('shape_leng', models.FloatField()),
                ('shape_area', models.FloatField()),
                ('geom', django.contrib.gis.db.models.fields.MultiPolygonField(srid=4326)),
            ],
        ),
    ]
