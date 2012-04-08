# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'SearchCache.search_time'
        db.add_column('search_searchcache', 'search_time',
                      self.gf('django.db.models.fields.DateTimeField')(auto_now=True, default=datetime.datetime(2012, 4, 7, 0, 0), blank=True),
                      keep_default=False)

    def backwards(self, orm):
        # Deleting field 'SearchCache.search_time'
        db.delete_column('search_searchcache', 'search_time')

    models = {
        'bn.metrostation': {
            'Meta': {'object_name': 'MetroStation'},
            'bn_id': ('django.db.models.fields.IntegerField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '64'})
        },
        'search.searchcache': {
            'Meta': {'object_name': 'SearchCache'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'metro_stations': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['bn.MetroStation']", 'symmetrical': 'False', 'blank': 'True'}),
            'price_from': ('django.db.models.fields.IntegerField', [], {'blank': 'True'}),
            'price_to': ('django.db.models.fields.IntegerField', [], {'blank': 'True'}),
            'rooms_from': ('django.db.models.fields.IntegerField', [], {'blank': 'True'}),
            'rooms_to': ('django.db.models.fields.IntegerField', [], {'blank': 'True'}),
            'search_time': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'})
        }
    }

    complete_apps = ['search']