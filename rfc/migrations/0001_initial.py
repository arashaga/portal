# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'RFCDocument'
        db.create_table(u'rfc_rfcdocument', (
            ('rfc_number', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('rfc_title', self.gf('django.db.models.fields.CharField')(max_length=254, null=True)),
            ('rfc_project', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['project.Projects'], unique=True)),
            ('rfc_issued_to', self.gf('django.db.models.fields.related.OneToOneField')(related_name='rfc_issued_to', unique=True, to=orm['signup.SignUp'])),
            ('rfc_drawing_detail_number', self.gf('django.db.models.fields.CharField')(max_length=5, null=True, blank=True)),
            ('rfc_specification_section', self.gf('django.db.models.fields.CharField')(max_length=20, null=True, blank=True)),
            ('rfc_drawing_page_number', self.gf('django.db.models.fields.CharField')(max_length=15, null=True, blank=True)),
            ('rfc_question', self.gf('django.db.models.fields.TextField')()),
            ('rfc_issued_by', self.gf('django.db.models.fields.related.OneToOneField')(related_name='rfc_issued_by', unique=True, to=orm['signup.SignUp'])),
            ('rfc_issued_date', self.gf('django.db.models.fields.DateField')(auto_now=True, blank=True)),
            ('rfc_answer', self.gf('django.db.models.fields.TextField')()),
            ('rfc_required_fls_review', self.gf('django.db.models.fields.BooleanField')()),
            ('rfc_required_sketch', self.gf('django.db.models.fields.BooleanField')()),
            ('rfc_required_fcd', self.gf('django.db.models.fields.BooleanField')()),
            ('rfc_answer_reviewed_by', self.gf('django.db.models.fields.related.OneToOneField')(related_name='rfc_ans_rev_by', unique=True, to=orm['signup.SignUp'])),
            ('rfc_answered_date_architect', self.gf('django.db.models.fields.DateField')(auto_now=True, blank=True)),
            ('rfc_answer_authorized_by', self.gf('django.db.models.fields.related.OneToOneField')(related_name='rfc_ans_auth_by', unique=True, to=orm['signup.SignUp'])),
            ('rfc_answer_issued_date', self.gf('django.db.models.fields.DateField')(auto_now=True, blank=True)),
        ))
        db.send_create_signal(u'rfc', ['RFCDocument'])


    def backwards(self, orm):
        # Deleting model 'RFCDocument'
        db.delete_table(u'rfc_rfcdocument')


    models = {
        u'address.addresses': {
            'Meta': {'object_name': 'Addresses'},
            'address': ('django.db.models.fields.CharField', [], {'max_length': '120', 'null': 'True', 'blank': 'True'}),
            'city': ('django.db.models.fields.CharField', [], {'max_length': '120', 'null': 'True', 'blank': 'True'}),
            'date_modified': ('django.db.models.fields.DateField', [], {'auto_now': 'True', 'blank': 'True'}),
            'fax': ('django.db.models.fields.CharField', [], {'max_length': '120', 'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'phone': ('django.db.models.fields.CharField', [], {'max_length': '120', 'null': 'True', 'blank': 'True'}),
            'state': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['state.States']"}),
            'website': ('django.db.models.fields.URLField', [], {'max_length': '200'})
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
        u'project.projects': {
            'Meta': {'object_name': 'Projects'},
            'Project_creation_date': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'project_active': ('django.db.models.fields.BooleanField', [], {}),
            'project_address': ('django.db.models.fields.CharField', [], {'max_length': '120', 'null': 'True', 'blank': 'True'}),
            'project_city': ('django.db.models.fields.CharField', [], {'max_length': '120', 'null': 'True', 'blank': 'True'}),
            'project_finish': ('django.db.models.fields.DateField', [], {}),
            'project_name': ('django.db.models.fields.CharField', [], {'max_length': '120'}),
            'project_number': ('django.db.models.fields.IntegerField', [], {'null': 'True'}),
            'project_owner': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['company.Companies']"}),
            'project_start': ('django.db.models.fields.DateField', [], {}),
            'project_state': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['state.States']"}),
            'project_title': ('django.db.models.fields.CharField', [], {'max_length': '120'})
        },
        u'rfc.rfcdocument': {
            'Meta': {'object_name': 'RFCDocument'},
            'rfc_answer': ('django.db.models.fields.TextField', [], {}),
            'rfc_answer_authorized_by': ('django.db.models.fields.related.OneToOneField', [], {'related_name': "'rfc_ans_auth_by'", 'unique': 'True', 'to': u"orm['signup.SignUp']"}),
            'rfc_answer_issued_date': ('django.db.models.fields.DateField', [], {'auto_now': 'True', 'blank': 'True'}),
            'rfc_answer_reviewed_by': ('django.db.models.fields.related.OneToOneField', [], {'related_name': "'rfc_ans_rev_by'", 'unique': 'True', 'to': u"orm['signup.SignUp']"}),
            'rfc_answered_date_architect': ('django.db.models.fields.DateField', [], {'auto_now': 'True', 'blank': 'True'}),
            'rfc_drawing_detail_number': ('django.db.models.fields.CharField', [], {'max_length': '5', 'null': 'True', 'blank': 'True'}),
            'rfc_drawing_page_number': ('django.db.models.fields.CharField', [], {'max_length': '15', 'null': 'True', 'blank': 'True'}),
            'rfc_issued_by': ('django.db.models.fields.related.OneToOneField', [], {'related_name': "'rfc_issued_by'", 'unique': 'True', 'to': u"orm['signup.SignUp']"}),
            'rfc_issued_date': ('django.db.models.fields.DateField', [], {'auto_now': 'True', 'blank': 'True'}),
            'rfc_issued_to': ('django.db.models.fields.related.OneToOneField', [], {'related_name': "'rfc_issued_to'", 'unique': 'True', 'to': u"orm['signup.SignUp']"}),
            'rfc_number': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'rfc_project': ('django.db.models.fields.related.OneToOneField', [], {'to': u"orm['project.Projects']", 'unique': 'True'}),
            'rfc_question': ('django.db.models.fields.TextField', [], {}),
            'rfc_required_fcd': ('django.db.models.fields.BooleanField', [], {}),
            'rfc_required_fls_review': ('django.db.models.fields.BooleanField', [], {}),
            'rfc_required_sketch': ('django.db.models.fields.BooleanField', [], {}),
            'rfc_specification_section': ('django.db.models.fields.CharField', [], {'max_length': '20', 'null': 'True', 'blank': 'True'}),
            'rfc_title': ('django.db.models.fields.CharField', [], {'max_length': '254', 'null': 'True'})
        },
        u'signup.signup': {
            'Meta': {'object_name': 'SignUp'},
            'address': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['address.Addresses']", 'null': 'True', 'blank': 'True'}),
            'date_joined': ('django.db.models.fields.DateField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'email': ('django.db.models.fields.EmailField', [], {'unique': 'True', 'max_length': '254', 'db_index': 'True'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '120', 'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'is_admin': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'last_login': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '120', 'null': 'True', 'blank': 'True'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '128'})
        },
        u'state.states': {
            'Meta': {'object_name': 'States'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'state_abv': ('django.db.models.fields.CharField', [], {'max_length': '2'})
        }
    }

    complete_apps = ['rfc']