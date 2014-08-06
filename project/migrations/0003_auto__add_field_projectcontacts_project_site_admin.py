# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):
    def forwards(self, orm):
        # Adding field 'ProjectContacts.project_site_admin'
        db.add_column(u'project_projectcontacts', 'project_site_admin',
                      self.gf('django.db.models.fields.BooleanField')(default=False),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'ProjectContacts.project_site_admin'
        db.delete_column(u'project_projectcontacts', 'project_site_admin')


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
            'website': ('django.db.models.fields.URLField', [], {'max_length': '200'})
        },
        u'auth.group': {
            'Meta': {'object_name': 'Group'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '80'}),
            'permissions': ('django.db.models.fields.related.ManyToManyField', [],
                            {'to': u"orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'})
        },
        u'auth.permission': {
            'Meta': {'ordering': "(u'content_type__app_label', u'content_type__model', u'codename')",
                     'unique_together': "((u'content_type', u'codename'),)", 'object_name': 'Permission'},
            'codename': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'content_type': (
            'django.db.models.fields.related.ForeignKey', [], {'to': u"orm['contenttypes.ContentType']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        u'company.companies': {
            'Meta': {'object_name': 'Companies'},
            'company_abv': ('django.db.models.fields.CharField', [], {'max_length': '10'}),
            'company_address': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['address.Addresses']"}),
            'company_name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '120'}),
            'date_modified': ('django.db.models.fields.DateField', [], {'auto_now': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_public': ('django.db.models.fields.BooleanField', [], {})
        },
        u'contenttypes.contenttype': {
            'Meta': {'ordering': "('name',)", 'unique_together': "(('app_label', 'model'),)",
                     'object_name': 'ContentType', 'db_table': "'django_content_type'"},
            'app_label': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        u'project.projectcontacts': {
            'Meta': {'object_name': 'ProjectContacts'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'project_contact': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['signup.SignUp']"}),
            'project_contact_add_date': (
            'django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'project_contact_group': (
            'django.db.models.fields.related.ForeignKey', [], {'to': u"orm['project.ProjectGroup']"}),
            'project_contact_title': (
            'django.db.models.fields.related.ForeignKey', [], {'to': u"orm['project.ProjectContactTitles']"}),
            'project_site_admin': ('django.db.models.fields.BooleanField', [], {'default': 'False'})
        },
        u'project.projectcontacttitles': {
            'Meta': {'object_name': 'ProjectContactTitles'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'project_contact_title': ('django.db.models.fields.CharField', [], {'max_length': '10'}),
            'project_contact_title_description': ('django.db.models.fields.CharField', [], {'max_length': '120'})
        },
        u'project.projectgroup': {
            'Meta': {'object_name': 'ProjectGroup'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'project_group_abrv': ('django.db.models.fields.CharField', [], {'max_length': '20'}),
            'project_group_description': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'project_group_timestamp': (
            'django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'})
        },
        u'project.projects': {
            'Meta': {'object_name': 'Projects'},
            'Project_creation_date': (
            'django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'project_active': ('django.db.models.fields.BooleanField', [], {}),
            'project_address': (
            'django.db.models.fields.CharField', [], {'max_length': '120', 'null': 'True', 'blank': 'True'}),
            'project_city': (
            'django.db.models.fields.CharField', [], {'max_length': '120', 'null': 'True', 'blank': 'True'}),
            'project_finish': ('django.db.models.fields.DateField', [], {}),
            'project_name': ('django.db.models.fields.CharField', [], {'max_length': '120'}),
            'project_number': ('django.db.models.fields.IntegerField', [], {'null': 'True'}),
            'project_owner': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['company.Companies']"}),
            'project_start': ('django.db.models.fields.DateField', [], {}),
            'project_state': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['state.States']"}),
            'project_title': ('django.db.models.fields.CharField', [], {'max_length': '120'})
        },
        u'signup.signup': {
            'Meta': {'object_name': 'SignUp'},
            'address': ('django.db.models.fields.related.ForeignKey', [],
                        {'to': u"orm['address.Addresses']", 'null': 'True', 'blank': 'True'}),
            'date_joined': ('django.db.models.fields.DateField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'email': (
            'django.db.models.fields.EmailField', [], {'unique': 'True', 'max_length': '254', 'db_index': 'True'}),
            'first_name': (
            'django.db.models.fields.CharField', [], {'max_length': '120', 'null': 'True', 'blank': 'True'}),
            'groups': ('django.db.models.fields.related.ManyToManyField', [],
                       {'symmetrical': 'False', 'related_name': "u'user_set'", 'blank': 'True',
                        'to': u"orm['auth.Group']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'is_admin': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_superuser': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'last_login': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'last_name': (
            'django.db.models.fields.CharField', [], {'max_length': '120', 'null': 'True', 'blank': 'True'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'user_permissions': ('django.db.models.fields.related.ManyToManyField', [],
                                 {'symmetrical': 'False', 'related_name': "u'user_set'", 'blank': 'True',
                                  'to': u"orm['auth.Permission']"})
        },
        u'state.states': {
            'Meta': {'object_name': 'States'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'state_abv': ('django.db.models.fields.CharField', [], {'max_length': '2'})
        }
    }

    complete_apps = ['project']