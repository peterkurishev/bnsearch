# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding M2M table for field flats on 'SearchCache'
        db.create_table('search_searchcache_flats', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('searchcache', models.ForeignKey(orm['search.searchcache'], null=False)),
            ('flat', models.ForeignKey(orm['bn.flat'], null=False))
        ))
        db.create_unique('search_searchcache_flats', ['searchcache_id', 'flat_id'])

    def backwards(self, orm):
        # Removing M2M table for field flats on 'SearchCache'
        db.delete_table('search_searchcache_flats')

    models = {
        'bn.edition': {
            'Meta': {'object_name': 'Edition'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '128'})
        },
        'bn.flat': {
            'Meta': {'object_name': 'Flat'},
            'additional': ('django.db.models.fields.CharField', [], {'max_length': '256'}),
            'address': ('django.db.models.fields.CharField', [], {'max_length': '256'}),
            'edition': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['bn.Edition']"}),
            'house_type': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['bn.HouseType']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'kitchen_s2': ('django.db.models.fields.FloatField', [], {}),
            'kontact': ('django.db.models.fields.CharField', [], {'max_length': '64'}),
            'level': ('django.db.models.fields.IntegerField', [], {}),
            'living_s2': ('django.db.models.fields.FloatField', [], {}),
            'metro_station': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['bn.MetroStation']"}),
            'phone': ('django.db.models.fields.CharField', [], {'max_length': '16'}),
            'rooms_number': ('django.db.models.fields.IntegerField', [], {}),
            'subject': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['bn.Subject']"}),
            'toilet': ('django.db.models.fields.CharField', [], {'max_length': '2'}),
            'whole_s2': ('django.db.models.fields.FloatField', [], {})
        },
        'bn.housetype': {
            'Meta': {'object_name': 'HouseType'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '16'})
        },
        'bn.metrostation': {
            'Meta': {'object_name': 'MetroStation'},
            'bn_id': ('django.db.models.fields.IntegerField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '64'})
        },
        'bn.subject': {
            'Meta': {'object_name': 'Subject'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '128'})
        },
        'search.searchcache': {
            'Meta': {'object_name': 'SearchCache'},
            'flats': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'to': "orm['bn.Flat']", 'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'metro_stations': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'to': "orm['bn.MetroStation']", 'null': 'True', 'blank': 'True'}),
            'price_from': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'price_to': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'rooms_from': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'rooms_to': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'search_time': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'})
        }
    }

    complete_apps = ['search']