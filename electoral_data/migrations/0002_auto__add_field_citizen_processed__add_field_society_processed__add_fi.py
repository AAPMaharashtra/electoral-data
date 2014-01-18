# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'Citizen.processed'
        db.add_column(u'electoral_data_citizen', 'processed',
                      self.gf('django.db.models.fields.BooleanField')(default=False),
                      keep_default=False)

        # Adding field 'Society.processed'
        db.add_column(u'electoral_data_society', 'processed',
                      self.gf('django.db.models.fields.BooleanField')(default=False),
                      keep_default=False)

        # Adding field 'PollingStation.processed'
        db.add_column(u'electoral_data_pollingstation', 'processed',
                      self.gf('django.db.models.fields.BooleanField')(default=False),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'Citizen.processed'
        db.delete_column(u'electoral_data_citizen', 'processed')

        # Deleting field 'Society.processed'
        db.delete_column(u'electoral_data_society', 'processed')

        # Deleting field 'PollingStation.processed'
        db.delete_column(u'electoral_data_pollingstation', 'processed')


    models = {
        u'electoral_data.assemblyconstituency': {
            'Meta': {'object_name': 'AssemblyConstituency'},
            'constituency_no': ('django.db.models.fields.CharField', [], {'max_length': '10', 'primary_key': 'True'}),
            'lok_sabha_seat': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['electoral_data.LokSabhaSeat']"}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        u'electoral_data.citizen': {
            'Meta': {'object_name': 'Citizen'},
            'age': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'interest': ('django.db.models.fields.CharField', [], {'default': "'neutral'", 'max_length': '10'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'parent_name': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'photo_available': ('django.db.models.fields.CharField', [], {'default': "'n'", 'max_length': '2'}),
            'processed': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'sex': ('django.db.models.fields.CharField', [], {'default': "'male'", 'max_length': '10'}),
            'society': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['electoral_data.Society']"}),
            't_flag': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'voter_id': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '100'})
        },
        u'electoral_data.loksabhaseat': {
            'Meta': {'object_name': 'LokSabhaSeat'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        u'electoral_data.pollingstation': {
            'Meta': {'object_name': 'PollingStation'},
            'constituency': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['electoral_data.AssemblyConstituency']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'processed': ('django.db.models.fields.BooleanField', [], {'default': 'False'})
        },
        u'electoral_data.society': {
            'Meta': {'object_name': 'Society'},
            'address': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'female_count': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'male_count': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'part_no': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '10'}),
            'pincode': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'polling_station': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['electoral_data.PollingStation']"}),
            'processed': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'society_no': ('django.db.models.fields.CharField', [], {'max_length': '50', 'primary_key': 'True'}),
            'total_count': ('django.db.models.fields.IntegerField', [], {'default': '0'})
        }
    }

    complete_apps = ['electoral_data']