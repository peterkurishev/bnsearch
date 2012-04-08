# -*- coding: utf-8 -*-
import models
from django.conf import settings
import urllib2
import lxml.html
import types

PARAM_MAP = {
    'price_from': 'price1',
    'price_to': 'price2',
    'rooms_from': 'kkv_1',
    'rooms_to': 'kkv_2',
    'metro_stations': 'metro',
    }

class BN(object):

    def __prepare_opener__(self):
        opener = urllib2.build_opener()
        opener.addheaders = [('User-agent', settings.USER_AGENT)]
        return opener

    def __get_url__(self, url):
        opener = self.__prepare_opener__()
        return opener.open(url)

    def get_metro_stations(self):
        '''
        Функция возвращает список моделей станций метро
        '''
        stations = []
        html = lxml.html.fromstring(self.__get_url__(settings.GET_METRO_URL).read())
        html_stations = html.cssselect('select#metro option')

        for html_station in html_stations:
            value = html_station.attrib['value']
            if value == '-1':
                continue
            station = models.MetroStation()
            station.name = html_station.text
            station.bn_id = value
            stations.append(station)
        return stations

    def get_flats(self, query):
        '''
        Ужасно длинная функция, которая возвращает квартиры
        '''
        flats = []
        url = settings.GET_FLATS_URL
        for key in query:
            value = query[key]
            if type(value) is types.NoneType:
                continue
            elif str(type(value)) == "<class 'django.db.models.query.QuerySet'>":
                for station in value:
                    url += '&'+PARAM_MAP[key]+'[]='+str(station.bn_id)
            elif type(value) is int:
                url += '&'+PARAM_MAP[key]+'='+str(value)
            else:
                print key
                print type(value)
                continue
                # raise Exception('Not a correct value type in query: %s' % str(type(value)))
        url = url.replace('&', '?', 1)

        html = lxml.html.fromstring(self.__get_url__(url).read())
        flat_links = html.xpath('//table[@class="results"]/tr/td/a[starts-with(@href,"/detail/")]/@href')

        for flat_link in flat_links:
            flat = models.Flat()
            contact = flat_link.getparent().getparent().getparent().xpath('td[last()-1]/text()')[0]
            flat.contact = contact
            
        
        # flat = models.Flat()
        # flats.append(flat)
        return flats

bn = BN()
