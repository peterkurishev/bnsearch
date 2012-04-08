# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Edition'
        db.create_table('bn_edition', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=128)),
        ))
        db.send_create_signal('bn', ['Edition'])

        # Adding field 'Flat.edition'
        db.add_column('bn_flat', 'edition',
                      self.gf('django.db.models.fields.related.ForeignKey')(default=0, to=orm['bn.Edition']),
                      keep_default=False)

        # Adding field 'Flat.rooms_number'
        db.add_column('bn_flat', 'rooms_number',
                      self.gf('django.db.models.fields.IntegerField')(default=1),
                      keep_default=False)

        # Adding field 'Flat.address'
        db.add_column('bn_flat', 'address',
                      self.gf('django.db.models.fields.CharField')(default='', max_length=256),
                      keep_default=False)

        # Adding field 'Flat.metro_station'
        db.add_column('bn_flat', 'metro_station',
                      self.gf('django.db.models.fields.related.ForeignKey')(default=0, to=orm['bn.MetroStation']),
                      keep_default=False)

    def backwards(self, orm):
        # Deleting model 'Edition'
        db.delete_table('bn_edition')

        # Deleting field 'Flat.edition'
        db.delete_column('bn_flat', 'edition_id')

        # Deleting field 'Flat.rooms_number'
        db.delete_column('bn_flat', 'rooms_number')

        # Deleting field 'Flat.address'
        db.delete_column('bn_flat', 'address')

        # Deleting field 'Flat.metro_station'
        db.delete_column('bn_flat', 'metro_station_id')

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
        }
    }

    complete_apps = ['bn']