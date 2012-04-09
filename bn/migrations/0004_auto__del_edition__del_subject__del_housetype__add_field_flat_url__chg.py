# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Deleting model 'Edition'
        db.delete_table('bn_edition')

        # Deleting model 'Subject'
        db.delete_table('bn_subject')

        # Deleting model 'HouseType'
        db.delete_table('bn_housetype')

        # Adding field 'Flat.url'
        db.add_column('bn_flat', 'url',
                      self.gf('django.db.models.fields.CharField')(default=u'http://www.bn.ru', max_length=1024),
                      keep_default=False)


        # Changing field 'Flat.toilet'
        db.alter_column('bn_flat', 'toilet', self.gf('django.db.models.fields.CharField')(max_length=16))

        # Changing field 'Flat.rooms_number'
        db.alter_column('bn_flat', 'rooms_number', self.gf('django.db.models.fields.CharField')(max_length=3))

        # Changing field 'Flat.level'
        db.alter_column('bn_flat', 'level', self.gf('django.db.models.fields.CharField')(max_length=16))

        # Changing field 'Flat.whole_s2'
        db.alter_column('bn_flat', 'whole_s2', self.gf('django.db.models.fields.CharField')(max_length=5))

        # Renaming column for 'Flat.edition' to match new field type.
        db.rename_column('bn_flat', 'edition_id', 'edition')
        # Changing field 'Flat.edition'
        db.alter_column('bn_flat', 'edition', self.gf('django.db.models.fields.CharField')(max_length=64))
        # Removing index on 'Flat', fields ['edition']
        db.delete_index('bn_flat', ['edition_id'])


        # Renaming column for 'Flat.metro_station' to match new field type.
        db.rename_column('bn_flat', 'metro_station_id', 'metro_station')
        # Changing field 'Flat.metro_station'
        db.alter_column('bn_flat', 'metro_station', self.gf('django.db.models.fields.CharField')(max_length=32))
        # Removing index on 'Flat', fields ['metro_station']
        db.delete_index('bn_flat', ['metro_station_id'])


        # Renaming column for 'Flat.house_type' to match new field type.
        db.rename_column('bn_flat', 'house_type_id', 'house_type')
        # Changing field 'Flat.house_type'
        db.alter_column('bn_flat', 'house_type', self.gf('django.db.models.fields.CharField')(max_length=32))
        # Removing index on 'Flat', fields ['house_type']
        db.delete_index('bn_flat', ['house_type_id'])


        # Changing field 'Flat.kitchen_s2'
        db.alter_column('bn_flat', 'kitchen_s2', self.gf('django.db.models.fields.CharField')(max_length=5))

        # Changing field 'Flat.living_s2'
        db.alter_column('bn_flat', 'living_s2', self.gf('django.db.models.fields.CharField')(max_length=5))

        # Renaming column for 'Flat.subject' to match new field type.
        db.rename_column('bn_flat', 'subject_id', 'subject')
        # Changing field 'Flat.subject'
        db.alter_column('bn_flat', 'subject', self.gf('django.db.models.fields.CharField')(max_length=128))
        # Removing index on 'Flat', fields ['subject']
        db.delete_index('bn_flat', ['subject_id'])

    def backwards(self, orm):
        # Adding index on 'Flat', fields ['subject']
        db.create_index('bn_flat', ['subject_id'])

        # Adding index on 'Flat', fields ['house_type']
        db.create_index('bn_flat', ['house_type_id'])

        # Adding index on 'Flat', fields ['metro_station']
        db.create_index('bn_flat', ['metro_station_id'])

        # Adding index on 'Flat', fields ['edition']
        db.create_index('bn_flat', ['edition_id'])

        # Adding model 'Edition'
        db.create_table('bn_edition', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=128)),
        ))
        db.send_create_signal('bn', ['Edition'])

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

        # Deleting field 'Flat.url'
        db.delete_column('bn_flat', 'url')


        # Changing field 'Flat.toilet'
        db.alter_column('bn_flat', 'toilet', self.gf('django.db.models.fields.CharField')(max_length=2))

        # Changing field 'Flat.rooms_number'
        db.alter_column('bn_flat', 'rooms_number', self.gf('django.db.models.fields.IntegerField')())

        # Changing field 'Flat.level'
        db.alter_column('bn_flat', 'level', self.gf('django.db.models.fields.IntegerField')())

        # Changing field 'Flat.whole_s2'
        db.alter_column('bn_flat', 'whole_s2', self.gf('django.db.models.fields.FloatField')())

        # Renaming column for 'Flat.edition' to match new field type.
        db.rename_column('bn_flat', 'edition', 'edition_id')
        # Changing field 'Flat.edition'
        db.alter_column('bn_flat', 'edition_id', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['bn.Edition']))

        # Renaming column for 'Flat.metro_station' to match new field type.
        db.rename_column('bn_flat', 'metro_station', 'metro_station_id')
        # Changing field 'Flat.metro_station'
        db.alter_column('bn_flat', 'metro_station_id', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['bn.MetroStation']))

        # Renaming column for 'Flat.house_type' to match new field type.
        db.rename_column('bn_flat', 'house_type', 'house_type_id')
        # Changing field 'Flat.house_type'
        db.alter_column('bn_flat', 'house_type_id', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['bn.HouseType']))

        # Changing field 'Flat.kitchen_s2'
        db.alter_column('bn_flat', 'kitchen_s2', self.gf('django.db.models.fields.FloatField')())

        # Changing field 'Flat.living_s2'
        db.alter_column('bn_flat', 'living_s2', self.gf('django.db.models.fields.FloatField')())

        # Renaming column for 'Flat.subject' to match new field type.
        db.rename_column('bn_flat', 'subject', 'subject_id')
        # Changing field 'Flat.subject'
        db.alter_column('bn_flat', 'subject_id', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['bn.Subject']))
    models = {
        'bn.flat': {
            'Meta': {'object_name': 'Flat'},
            'additional': ('django.db.models.fields.CharField', [], {'max_length': '256'}),
            'address': ('django.db.models.fields.CharField', [], {'max_length': '256'}),
            'edition': ('django.db.models.fields.CharField', [], {'max_length': '64'}),
            'house_type': ('django.db.models.fields.CharField', [], {'max_length': '32'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'kitchen_s2': ('django.db.models.fields.CharField', [], {'max_length': '5'}),
            'kontact': ('django.db.models.fields.CharField', [], {'max_length': '64'}),
            'level': ('django.db.models.fields.CharField', [], {'max_length': '16'}),
            'living_s2': ('django.db.models.fields.CharField', [], {'max_length': '5'}),
            'metro_station': ('django.db.models.fields.CharField', [], {'max_length': '32'}),
            'phone': ('django.db.models.fields.CharField', [], {'max_length': '16'}),
            'rooms_number': ('django.db.models.fields.CharField', [], {'max_length': '3'}),
            'subject': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'toilet': ('django.db.models.fields.CharField', [], {'max_length': '16'}),
            'url': ('django.db.models.fields.CharField', [], {'max_length': '1024'}),
            'whole_s2': ('django.db.models.fields.CharField', [], {'max_length': '5'})
        },
        'bn.metrostation': {
            'Meta': {'object_name': 'MetroStation'},
            'bn_id': ('django.db.models.fields.IntegerField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '64'})
        }
    }

    complete_apps = ['bn']