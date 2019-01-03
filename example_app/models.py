# -*- coding: utf-8 -*
import datetime
from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User, Group
from django.template.defaultfilters import slugify
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User

class Artist(models.Model):
    none = models.IntegerField(default=-1000)
    name = models.CharField(blank=True, null=True, max_length=122100)
    text = models.CharField(blank=True, null=True, max_length=122100)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True,
                             related_name="artist")

    def save(self, *args, **kwargs):
        super(Artist, self).save(*args, **kwargs)

    def __str__(self):
        return self.name

class Prod(models.Model):
    none = models.IntegerField(default=-1000)
    name = models.CharField(blank=True, null=True, max_length=122100)
    idv = models.CharField(blank=True, null=True, max_length=122100)
    cover = models.CharField(blank=True, null=True, max_length=122100)


    def save(self, *args, **kwargs):
        names=str(self.name)
        super(Prod, self).save(*args, **kwargs)

    def __str__(self):
        return self.name
"""
Prod.objects.create(name="Product A", idv="+1", cover="High")
Prod.objects.create(name="Product B", idv="-1", cover="High")
Prod.objects.create(name="Product C", idv="+1", cover="Low")
Prod.objects.create(name="Product D", idv="-1", cover="Low")

print("Prod")
"""

class Make(models.Model):
    none = models.IntegerField(default=-1000)
    name = models.CharField(blank=True, null=True, max_length=122100)
    namec = models.CharField(blank=True, null=True, max_length=122100)
    model = models.CharField(blank=True, null=True, max_length=122100)
    modelc = models.CharField(blank=True, null=True, max_length=122100)
    cc = models.CharField(blank=True, null=True, max_length=122100)
    name1 = models.CharField(blank=True, null=True, max_length=122100)
    exprice = models.DecimalField(max_digits=30, default=0,decimal_places=3, blank=True, null=True)
    start_date = models.CharField(blank=True, null=True, max_length=122100)

    def save(self, *args, **kwargs):
        name=str(self.name).upper()
        model=str(self.model).upper()
        cc=str(self.cc).upper()
        name1=str(self.name1).upper()
        super(Make, self).save(*args, **kwargs)

    def __str__(self):
        return self.model

class RTO(models.Model):
    none = models.IntegerField(default=-1000)
    loct = models.CharField(blank=True, null=True, max_length=122100)
    loct_code = models.CharField(blank=True, null=True, max_length=122100)
    state_code = models.CharField(blank=True, null=True, max_length=122100)
    city_code = models.CharField(blank=True, null=True, max_length=122100)

    def save(self, *args, **kwargs):
        loct=str(self.loct).upper().strip()
        loct_code=str(self.loct_code).upper().strip()
        super(RTO, self).save(*args, **kwargs)

    def __str__(self):
        return self.loct