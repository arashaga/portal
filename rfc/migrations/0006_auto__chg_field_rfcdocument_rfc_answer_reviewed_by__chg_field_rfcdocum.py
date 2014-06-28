# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):

        # Changing field 'RFCDocument.rfc_answer_reviewed_by'
        db.alter_column(u'rfc_rfcdocument', 'rfc_answer_reviewed_by_id', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['project.ProjectContacts']))

        # Changing field 'RFCDocument.rfc_answer_authorized_by'
        db.alter_column(u'rfc_rfcdocument', 'rfc_answer_authorized_by_id', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['project.ProjectContacts']))

        # Changing field 'RFCDocument.rfc_issued_by'
        db.alter_column(u'rfc_rfcdocument', 'rfc_issued_by_id', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['project.ProjectContacts']))

        # Changing field 'RFCDocument.rfc_issued_to'
        db.alter_column(u'rfc_rfcdocument', 'rfc_issued_to_id', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['project.ProjectContacts']))

    def backwards(self, orm):

        # Changing field 'RFCDocument.rfc_answer_reviewed_by'
        db.alter_column(u'rfc_rfcdocument', 'rfc_answer_reviewed_by_id', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['signup.SignUp']))

        # Changing field 'RFCDocument.rfc_answer_authorized_by'
        db.alter_column(u'rfc_rfcdocument', 'rfc_answer_authorized_by_id', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['signup.SignUp']))

        # Changing field 'RFCDocument.rfc_issued_by'
        db.alter_column(u'rfc_rfcdocument', 'rfc_issued_by_id', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['signup.SignUp']))

        # Changing field 'RFCDocument.rfc_issued_to'
        db.alter_column(u'rfc_rfcdocument', 'rfc_issued_to_id', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['signup.SignUp']))

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
        u'project.projectcontacts': {
            'Meta': {'object_name': 'ProjectContacts'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'project_contact': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['signup.SignUp']"}),
            'project_contact_add_date': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'project_contact_group': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['project.ProjectGroup']"}),
            'project_contact_title': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['project.ProjectContactTitles']"})
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
            'project_group_timestamp': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'})
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
            'rfc_answer_authorized_by': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'rfc_ans_auth_by'", 'to': u"orm['project.ProjectContacts']"}),
            'rfc_answer_issued_date': ('django.db.models.fields.DateField', [], {'auto_now': 'True', 'blank': 'True'}),
            'rfc_answer_reviewed_by': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'rfc_ans_rev_by'", 'to': u"orm['project.ProjectContacts']"}),
            'rfc_answered_date_architect': ('django.db.models.fields.DateField', [], {'auto_now': 'True', 'blank': 'True'}),
            'rfc_drawing_detail_number': ('django.db.models.fields.CharField', [], {'max_length': '5', 'null': 'True', 'blank': 'True'}),
            'rfc_drawing_page_number': ('django.db.models.fields.CharField', [], {'max_length': '15', 'null': 'True', 'blank': 'True'}),
            'rfc_issued_by': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'rfc_issued_by'", 'to': u"orm['project.ProjectContacts']"}),
            'rfc_issued_date': ('django.db.models.fields.DateField', [], {'auto_now': 'True', 'blank': 'True'}),
            'rfc_issued_to': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'rfc_issued_to'", 'to': u"orm['project.ProjectContacts']"}),
            'rfc_number': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'rfc_project': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['project.Projects']"}),
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