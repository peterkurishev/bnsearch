import models
from django.conf import settings
import urllib2
import lxml.html

class BN(object):
    
    def get_metro_stations(self):
        stations = []
        # TODO: Get all metro stations from bn.ru here
        opener = urllib2.build_opener()
        opener.addheaders = [('User-agent', settings.USER_AGENT)]
        response = opener.open(settings.GET_METRO_URL)
        html = lxml.html.fromstring(response.read())
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
        flats = []
        # flat = models.Flat()
        # flats.append(flat)
        return flats

bn = BN()
