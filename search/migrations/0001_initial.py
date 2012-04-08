# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'SearchCache'
        db.create_table('search_searchcache', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('rooms_from', self.gf('django.db.models.fields.IntegerField')()),
            ('rooms_to', self.gf('django.db.models.fields.IntegerField')()),
            ('price_from', self.gf('django.db.models.fields.IntegerField')()),
            ('price_to', self.gf('django.db.models.fields.IntegerField')()),
        ))
        db.send_create_signal('search', ['SearchCache'])

        # Adding M2M table for field metro_stations on 'SearchCache'
        db.create_table('search_searchcache_metro_stations', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('searchcache', models.ForeignKey(orm['search.searchcache'], null=False)),
            ('metrostation', models.ForeignKey(orm['bn.metrostation'], null=False))
        ))
        db.create_unique('search_searchcache_metro_stations', ['searchcache_id', 'metrostation_id'])

    def backwards(self, orm):
        # Deleting model 'SearchCache'
        db.delete_table('search_searchcache')

        # Removing M2M table for field metro_stations on 'SearchCache'
        db.delete_table('search_searchcache_metro_stations')

    models = {
        'bn.metrostation': {
            'Meta': {'object_name': 'MetroStation'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '64'})
        },
        'search.searchcache': {
            'Meta': {'object_name': 'SearchCache'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'metro_stations': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['bn.MetroStation']", 'symmetrical': 'False'}),
            'price_from': ('django.db.models.fields.IntegerField', [], {}),
            'price_to': ('django.db.models.fields.IntegerField', [], {}),
            'rooms_from': ('django.db.models.fields.IntegerField', [], {}),
            'rooms_to': ('django.db.models.fields.IntegerField', [], {})
        }
    }

    complete_apps = ['search']