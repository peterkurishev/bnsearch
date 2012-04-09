# -*- coding: utf-8 -*-
import models
from django.conf import settings
import urllib2
import lxml.html
import types
import re

PARAM_MAP = {
    'price_from': 'price1',
    'price_to': 'price2',
    'rooms_from': 'kkv_1',
    'rooms_to': 'kkv_2',
    'metro_stations': 'metro',
    }

PRINT_PARAMS = [ u'Издание',
                 u'Комнат',
                 u'Дополнительно',
                 u'Санузел',
                 u'Тип дома',
                 u'Жилая пл. (м2)',
                 u'Пл. кухни (м2)',
                 u'Общая пл. (м2)',
                 u'Метро',
                 u'Этаж/ Этажность',
                 u'Комнат',
                 u'Адрес',
                 u'Телефон',
                 u'Контакт',
                 u'Субъект',
                 u'URL']


class BN(object):

    def __prepare_opener__(self):
        opener = urllib2.build_opener()
        opener.addheaders = [('User-agent', settings.USER_AGENT)]
        return opener

    def __get_url__(self, url):
        opener = self.__prepare_opener__()
        return opener.open(url)

    def __get_value_or_null__(self, mdict, key):
        try:
            return mdict[key]
        except:
            return ' '

    def __get_flat_details__(self, link, flat_params):
        '''
        Функция получает url страницы с информацией о
        квартире. Возвращает словарь название параметра (как на
        странице) -> значение
        '''
        url = settings.SITE_ROOT+link

        html = self.__get_url__(url)
        xhtml = lxml.html.fromstring(html.read())

        cells = xhtml.xpath(settings.DETAIL_CELLS_XPATH)

        result = dict()
        result[u'URL'] = url

        for i in range(len(cells)/2):
            value = cells.pop().text_content()
            name = cells.pop().text_content()
            name = re.sub(':', '', name)
            name = name.strip()
            if name in flat_params:
                result[name] = value
        return result

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
        Ужасно длинная функция, которая возвращает квартиры.
        FIXME: рефакторинг
        '''
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
                continue
        url = url.replace('&', '?', 1)

        html = lxml.html.fromstring(self.__get_url__(url).read())
        flat_links = html.xpath(settings.FLAT_LINKS_XPATH)

        flat_params = []
        
        for field in models.Flat._meta.fields:
            if field.name != 'id':
                flat_params.append(field.verbose_name)

        flats = []

        for flat_link in flat_links:
            flat = models.Flat()

            contact = ''
            try:
                contact = flat_link.getparent().getparent().getparent().xpath('td[last()-1]/text()')[0]
            except IndexError:
                pass
            params = self.__get_flat_details__(flat_link, flat_params)

            params[u'Контакт'] = contact

            for field in flat._meta.fields:
                if field.name != 'id':
                    setattr(flat, field.name, self.__get_value_or_null__(params, field.verbose_name))
            
            print flat
            flats.append(flat)
            

        return (flats, flat_params)

bn = BN()
