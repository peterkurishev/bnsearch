# -*- coding: utf-8 -*-

from django.db import models
from bn.utils import bn

class MetroStationManager(models.Manager):
    def get_query_set(self):
        if super(MetroStationManager, self).get_query_set().count() == 0:
            stations = bn.get_metro_stations()
            for station in stations:
                station.save()
        return super(MetroStationManager, self).get_query_set()

class FlatManager(models.Manager):
    pass
            

class MetroStation(models.Model):
    name = models.CharField(max_length=64)
    bn_id = models.IntegerField()
    objects = MetroStationManager()

    def __unicode__(self):
        return self.name

class Flat(models.Model):

    edition = models.CharField(u"Издание", max_length=64)
    rooms_number = models.CharField(u"Комнат", max_length=3)
    address = models.CharField(u"Адрес", max_length=256)
    metro_station = models.CharField(u"Метро", max_length=32)
    level = models.CharField(u"Этаж/ Этажность", max_length=16)
    house_type = models.CharField(u"Тип дома", max_length=32)
    whole_s2 = models.CharField(u"Общая пл. (м2)", max_length=5)
    living_s2 = models.CharField(u"Жилая пл. (м2)", max_length=5)
    kitchen_s2 = models.CharField(u"Пл. кухни (м2)", max_length=5)
    phone = models.CharField(u"Телефон", max_length=16)
    toilet = models.CharField(u"Санузел", max_length=16)
    subject = models.CharField(u'Субъект', max_length=128)
    kontact = models.CharField(u"Контакт", max_length = 64)
    additional = models.CharField(u"Дополнительно", max_length=256)
    url = models.CharField(u'URL', max_length=1024)

    def __unicode__(self):
        string = u'<tr>'
        for field in self._meta.fields:
            if field.name != 'id':
                string += u'<td>%s</td>' % (getattr(self, field.name),)
        string += u'</tr>'
        return string
