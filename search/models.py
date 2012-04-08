# -*- coding: utf-8 -*-
from django.db import models
from bn import models as bnmodels

class SearchCache(models.Model):
    rooms_from = models.IntegerField(u"Количество комнат от:", blank=True, null=True)
    rooms_to = models.IntegerField(u"до:", blank=True, null=True)
    price_from = models.IntegerField(u"Цена от:", blank=True, null=True)
    price_to = models.IntegerField(u"до", blank=True, null=True)
    metro_stations = models.ManyToManyField(bnmodels.MetroStation, blank=True, null=True)
    search_time = models.DateTimeField(editable=False, auto_now=True)
