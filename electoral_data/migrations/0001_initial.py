# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'LokSabhaSeat'
        db.create_table(u'electoral_data_loksabhaseat', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=100)),
        ))
        db.send_create_signal(u'electoral_data', ['LokSabhaSeat'])

        # Adding model 'AssemblyConstituency'
        db.create_table(u'electoral_data_assemblyconstituency', (
            ('lok_sabha_seat', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['electoral_data.LokSabhaSeat'])),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('constituency_no', self.gf('django.db.models.fields.CharField')(max_length=10, primary_key=True)),
        ))
        db.send_create_signal(u'electoral_data', ['AssemblyConstituency'])

        # Adding model 'PollingStation'
        db.create_table(u'electoral_data_pollingstation', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('constituency', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['electoral_data.AssemblyConstituency'])),
        ))
        db.send_create_signal(u'electoral_data', ['PollingStation'])

        # Adding model 'Society'
        db.create_table(u'electoral_data_society', (
            ('society_no', self.gf('django.db.models.fields.CharField')(max_length=50, primary_key=True)),
            ('part_no', self.gf('django.db.models.fields.CharField')(default='', max_length=10)),
            ('address', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('pincode', self.gf('django.db.models.fields.IntegerField')(default=0)),
            ('polling_station', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['electoral_data.PollingStation'])),
            ('male_count', self.gf('django.db.models.fields.IntegerField')(default=0)),
            ('female_count', self.gf('django.db.models.fields.IntegerField')(default=0)),
            ('total_count', self.gf('django.db.models.fields.IntegerField')(default=0)),
        ))
        db.send_create_signal(u'electoral_data', ['Society'])

        # Adding model 'Citizen'
        db.create_table(u'electoral_data_citizen', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('society', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['electoral_data.Society'])),
            ('voter_id', self.gf('django.db.models.fields.CharField')(default='', max_length=100)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('parent_name', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('t_flag', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('age', self.gf('django.db.models.fields.IntegerField')(default=0)),
            ('sex', self.gf('django.db.models.fields.CharField')(default='male', max_length=10)),
            ('interest', self.gf('django.db.models.fields.CharField')(default='neutral', max_length=10)),
            ('photo_available', self.gf('django.db.models.fields.CharField')(default='n', max_length=2)),
        ))
        db.send_create_signal(u'electoral_data', ['Citizen'])


    def backwards(self, orm):
        # Deleting model 'LokSabhaSeat'
        db.delete_table(u'electoral_data_loksabhaseat')

        # Deleting model 'AssemblyConstituency'
        db.delete_table(u'electoral_data_assemblyconstituency')

        # Deleting model 'PollingStation'
        db.delete_table(u'electoral_data_pollingstation')

        # Deleting model 'Society'
        db.delete_table(u'electoral_data_society')

        # Deleting model 'Citizen'
        db.delete_table(u'electoral_data_citizen')


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
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        u'electoral_data.society': {
            'Meta': {'object_name': 'Society'},
            'address': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'female_count': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'male_count': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'part_no': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '10'}),
            'pincode': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'polling_station': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['electoral_data.PollingStation']"}),
            'society_no': ('django.db.models.fields.CharField', [], {'max_length': '50', 'primary_key': 'True'}),
            'total_count': ('django.db.models.fields.IntegerField', [], {'default': '0'})
        }
    }

    complete_apps = ['electoral_data']