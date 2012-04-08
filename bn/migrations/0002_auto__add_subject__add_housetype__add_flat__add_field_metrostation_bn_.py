# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Subject'
        db.create_table('bn_subject', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=128)),
        ))
        db.send_create_signal('bn', ['Subject'])

        # Adding model 'HouseType'
        db.create_table('bn_housetype', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=16)),
        ))
        db.send_create_signal('bn', ['HouseType'])

        # Adding model 'Flat'
        db.create_table('bn_flat', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('level', self.gf('django.db.models.fields.IntegerField')()),
            ('house_type', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['bn.HouseType'])),
            ('whole_s2', self.gf('django.db.models.fields.FloatField')()),
            ('living_s2', self.gf('django.db.models.fields.FloatField')()),
            ('kitchen_s2', self.gf('django.db.models.fields.FloatField')()),
            ('phone', self.gf('django.db.models.fields.CharField')(max_length=16)),
            ('toilet', self.gf('django.db.models.fields.CharField')(max_length=2)),
            ('subject', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['bn.Subject'])),
            ('kontact', self.gf('django.db.models.fields.CharField')(max_length=64)),
            ('additional', self.gf('django.db.models.fields.CharField')(max_length=256)),
        ))
        db.send_create_signal('bn', ['Flat'])

        # Adding field 'MetroStation.bn_id'
        db.add_column('bn_metrostation', 'bn_id',
                      self.gf('django.db.models.fields.IntegerField')(default=0),
                      keep_default=False)

    def backwards(self, orm):
        # Deleting model 'Subject'
        db.delete_table('bn_subject')

        # Deleting model 'HouseType'
        db.delete_table('bn_housetype')

        # Deleting model 'Flat'
        db.delete_table('bn_flat')

        # Deleting field 'MetroStation.bn_id'
        db.delete_column('bn_metrostation', 'bn_id')

    models = {
        'bn.flat': {
            'Meta': {'object_name': 'Flat'},
            'additional': ('django.db.models.fields.CharField', [], {'max_length': '256'}),
            'house_type': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['bn.HouseType']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'kitchen_s2': ('django.db.models.fields.FloatField', [], {}),
            'kontact': ('django.db.models.fields.CharField', [], {'max_length': '64'}),
            'level': ('django.db.models.fields.IntegerField', [], {}),
            'living_s2': ('django.db.models.fields.FloatField', [], {}),
            'phone': ('django.db.models.fields.CharField', [], {'max_length': '16'}),
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