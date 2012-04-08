# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):

        # Changing field 'SearchCache.price_to'
        db.alter_column('search_searchcache', 'price_to', self.gf('django.db.models.fields.IntegerField')(null=True))

        # Changing field 'SearchCache.rooms_from'
        db.alter_column('search_searchcache', 'rooms_from', self.gf('django.db.models.fields.IntegerField')(null=True))

        # Changing field 'SearchCache.rooms_to'
        db.alter_column('search_searchcache', 'rooms_to', self.gf('django.db.models.fields.IntegerField')(null=True))

        # Changing field 'SearchCache.price_from'
        db.alter_column('search_searchcache', 'price_from', self.gf('django.db.models.fields.IntegerField')(null=True))
    def backwards(self, orm):

        # User chose to not deal with backwards NULL issues for 'SearchCache.price_to'
        raise RuntimeError("Cannot reverse this migration. 'SearchCache.price_to' and its values cannot be restored.")

        # User chose to not deal with backwards NULL issues for 'SearchCache.rooms_from'
        raise RuntimeError("Cannot reverse this migration. 'SearchCache.rooms_from' and its values cannot be restored.")

        # User chose to not deal with backwards NULL issues for 'SearchCache.rooms_to'
        raise RuntimeError("Cannot reverse this migration. 'SearchCache.rooms_to' and its values cannot be restored.")

        # User chose to not deal with backwards NULL issues for 'SearchCache.price_from'
        raise RuntimeError("Cannot reverse this migration. 'SearchCache.price_from' and its values cannot be restored.")
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
            'metro_stations': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'to': "orm['bn.MetroStation']", 'null': 'True', 'blank': 'True'}),
            'price_from': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'price_to': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'rooms_from': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'rooms_to': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'search_time': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'})
        }
    }

    complete_apps = ['search']