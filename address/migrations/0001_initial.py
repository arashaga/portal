# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):
    def forwards(self, orm):
        # Adding model 'Addresses'
        db.create_table(u'address_addresses', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('address', self.gf('django.db.models.fields.CharField')(max_length=120, null=True, blank=True)),
            ('city', self.gf('django.db.models.fields.CharField')(max_length=120, null=True, blank=True)),
            ('state', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['state.States'])),
            ('zipcode', self.gf('django.db.models.fields.CharField')(max_length=5)),
            ('phone', self.gf('django.db.models.fields.CharField')(max_length=120, null=True, blank=True)),
            ('fax', self.gf('django.db.models.fields.CharField')(max_length=120, null=True, blank=True)),
            ('website', self.gf('django.db.models.fields.URLField')(max_length=200)),
            ('date_modified', self.gf('django.db.models.fields.DateField')(auto_now=True, blank=True)),
        ))
        db.send_create_signal(u'address', ['Addresses'])


    def backwards(self, orm):
        # Deleting model 'Addresses'
        db.delete_table(u'address_addresses')


    models = {
        u'address.addresses': {
            'Meta': {'object_name': 'Addresses'},
            'address': (
            'django.db.models.fields.CharField', [], {'max_length': '120', 'null': 'True', 'blank': 'True'}),
            'city': ('django.db.models.fields.CharField', [], {'max_length': '120', 'null': 'True', 'blank': 'True'}),
            'date_modified': ('django.db.models.fields.DateField', [], {'auto_now': 'True', 'blank': 'True'}),
            'fax': ('django.db.models.fields.CharField', [], {'max_length': '120', 'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'phone': ('django.db.models.fields.CharField', [], {'max_length': '120', 'null': 'True', 'blank': 'True'}),
            'state': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['state.States']"}),
            'website': ('django.db.models.fields.URLField', [], {'max_length': '200'}),
            'zipcode': ('django.db.models.fields.CharField', [], {'max_length': '5'})
        },
        u'state.states': {
            'Meta': {'object_name': 'States'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'state_abv': ('django.db.models.fields.CharField', [], {'max_length': '2'})
        }
    }

    complete_apps = ['address']