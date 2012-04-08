# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'MetroStation'
        db.create_table('bn_metrostation', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=64)),
        ))
        db.send_create_signal('bn', ['MetroStation'])

    def backwards(self, orm):
        # Deleting model 'MetroStation'
        db.delete_table('bn_metrostation')

    models = {
        'bn.metrostation': {
            'Meta': {'object_name': 'MetroStation'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '64'})
        }
    }

    complete_apps = ['bn']