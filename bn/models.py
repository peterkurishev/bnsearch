# -*- coding: utf-8 -*-

from django.db import models
from bn.utils import bn

class MetroStationManager(models.Manager):
    def get_query_set(self):
        if super(MetroStationManager, self).get_query_set().count() == 0:
            # get objects from page here
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

class HouseType(models.Model):
    name = models.CharField(max_length=16)

class Subject(models.Model):
    name = models.CharField(max_length=128)

class Edition(models.Model):
    name = models.CharField(max_length=128)

class Flat(models.Model):
    TOILET_TYPES = (
        ('U', u"Неизвестно"),
        ('A', u"Совмещенный"),
        ('B', u"Раздельный"),
        )

    edition = models.ForeignKey(Edition)
    rooms_number = models.IntegerField(u"Количество комнат")
    address = models.CharField(u"Адрес", max_length=256)
    metro_station = models.ForeignKey(MetroStation)
    level = models.IntegerField(u"Этаж")
    house_type = models.ForeignKey(HouseType)
    whole_s2 = models.FloatField(u"Общая площадь")
    living_s2 = models.FloatField(u"Жилая площадь")
    kitchen_s2 = models.FloatField(u"Площадь кухни")
    phone = models.CharField(u"Телефон", max_length=16)
    toilet = models.CharField(u"Санузел", max_length=2, choices = TOILET_TYPES)
    subject = models.ForeignKey(Subject)
    kontact = models.CharField(u"Контакт", max_length = 64)
    additional = models.CharField(u"Дополнительная информация", max_length=256)

    # def save_with_dicts(self, house_type_name, subject_name, edition, metro):
    #     ht_id = 0
    #     try:
    #         ht_id = HouseType.objects.get(name=house_type_name)
    #     except:
    #         ht = HouseType(name=house_type_name)
    #         ht_id = ht.save()

    #     try:
    #         subject_id = Subject.objects.get(name=subject_name)
    #     except:
    #         ht = HouseType(name=house_type_name)
    #         ht_id = ht.save()
    #     try:
    #         ht_id = HouseType.objects.get(name=house_type_name)
    #     except:
    #         ht = HouseType(name=house_type_name)
    #         ht_id = ht.save()
