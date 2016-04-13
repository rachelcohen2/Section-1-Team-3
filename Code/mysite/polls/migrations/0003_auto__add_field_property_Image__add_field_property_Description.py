# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'property.Image'
        db.add_column(u'polls_property', 'Image',
                      self.gf('django.db.models.fields.CharField')(default='PLACEHOLDER', max_length=30),
                      keep_default=False)

        # Adding field 'property.Description'
        db.add_column(u'polls_property', 'Description',
                      self.gf('django.db.models.fields.CharField')(default='NO DESCRIPTION', max_length=256),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'property.Image'
        db.delete_column(u'polls_property', 'Image')

        # Deleting field 'property.Description'
        db.delete_column(u'polls_property', 'Description')


    models = {
        u'polls.property': {
            'Description': ('django.db.models.fields.CharField', [], {'max_length': '256'}),
            'Image': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            'Location': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'Meta': {'object_name': 'property'},
            'Name': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            'Owner': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            'Price': ('django.db.models.fields.FloatField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        }
    }

    complete_apps = ['polls']