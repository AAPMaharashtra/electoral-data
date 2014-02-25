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
            ('name', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('constituency', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['electoral_data.AssemblyConstituency'])),
            ('processed', self.gf('django.db.models.fields.BooleanField')(default=False)),
        ))
        db.send_create_signal(u'electoral_data', ['PollingStation'])

        # Adding model 'Citizen'
        db.create_table(u'electoral_data_citizen', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('polling_station', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['electoral_data.PollingStation'])),
            ('part_no', self.gf('django.db.models.fields.IntegerField')()),
            ('serial_no', self.gf('django.db.models.fields.IntegerField')()),
            ('voter_id', self.gf('django.db.models.fields.CharField')(default='', max_length=100)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('parent_name', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('house_no', self.gf('django.db.models.fields.CharField')(default='', max_length=100)),
            ('age', self.gf('django.db.models.fields.IntegerField')(default=0)),
            ('sex', self.gf('django.db.models.fields.CharField')(default='male', max_length=10)),
            ('interest', self.gf('django.db.models.fields.CharField')(default='neutral', max_length=10)),
            ('processed', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('isMember', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('member_no', self.gf('django.db.models.fields.CharField')(default='', max_length=20, blank=True)),
            ('email_address', self.gf('django.db.models.fields.EmailField')(max_length=75, blank=True)),
            ('isVolunteer', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('isDonor', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('voucher_no', self.gf('django.db.models.fields.CharField')(default='', max_length=100, blank=True)),
            ('donation_amount', self.gf('django.db.models.fields.IntegerField')(default=0)),
            ('markForDeletion', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('markForTransposition', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('phone_no', self.gf('django.db.models.fields.CharField')(default='', max_length=20, blank=True)),
        ))
        db.send_create_signal(u'electoral_data', ['Citizen'])

        # Adding model 'UserProfile'
        db.create_table(u'electoral_data_userprofile', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('user', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['auth.User'], unique=True)),
            ('polling_station', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['electoral_data.PollingStation'], null=True, blank=True)),
            ('assembly', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['electoral_data.AssemblyConstituency'], null=True, blank=True)),
        ))
        db.send_create_signal(u'electoral_data', ['UserProfile'])


    def backwards(self, orm):
        # Deleting model 'LokSabhaSeat'
        db.delete_table(u'electoral_data_loksabhaseat')

        # Deleting model 'AssemblyConstituency'
        db.delete_table(u'electoral_data_assemblyconstituency')

        # Deleting model 'PollingStation'
        db.delete_table(u'electoral_data_pollingstation')

        # Deleting model 'Citizen'
        db.delete_table(u'electoral_data_citizen')

        # Deleting model 'UserProfile'
        db.delete_table(u'electoral_data_userprofile')


    models = {
        u'auth.group': {
            'Meta': {'object_name': 'Group'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '80'}),
            'permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'})
        },
        u'auth.permission': {
            'Meta': {'ordering': "(u'content_type__app_label', u'content_type__model', u'codename')", 'unique_together': "((u'content_type', u'codename'),)", 'object_name': 'Permission'},
            'codename': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'content_type': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['contenttypes.ContentType']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        u'auth.user': {
            'Meta': {'object_name': 'User'},
            'date_joined': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'blank': 'True'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'groups': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'related_name': "u'user_set'", 'blank': 'True', 'to': u"orm['auth.Group']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'is_staff': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_superuser': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'last_login': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'user_permissions': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'related_name': "u'user_set'", 'blank': 'True', 'to': u"orm['auth.Permission']"}),
            'username': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '30'})
        },
        u'contenttypes.contenttype': {
            'Meta': {'ordering': "('name',)", 'unique_together': "(('app_label', 'model'),)", 'object_name': 'ContentType', 'db_table': "'django_content_type'"},
            'app_label': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        u'electoral_data.assemblyconstituency': {
            'Meta': {'object_name': 'AssemblyConstituency'},
            'constituency_no': ('django.db.models.fields.CharField', [], {'max_length': '10', 'primary_key': 'True'}),
            'lok_sabha_seat': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['electoral_data.LokSabhaSeat']"}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        u'electoral_data.citizen': {
            'Meta': {'object_name': 'Citizen'},
            'age': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'donation_amount': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'email_address': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'blank': 'True'}),
            'house_no': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '100'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'interest': ('django.db.models.fields.CharField', [], {'default': "'neutral'", 'max_length': '10'}),
            'isDonor': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'isMember': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'isVolunteer': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'markForDeletion': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'markForTransposition': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'member_no': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '20', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'parent_name': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'part_no': ('django.db.models.fields.IntegerField', [], {}),
            'phone_no': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '20', 'blank': 'True'}),
            'polling_station': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['electoral_data.PollingStation']"}),
            'processed': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'serial_no': ('django.db.models.fields.IntegerField', [], {}),
            'sex': ('django.db.models.fields.CharField', [], {'default': "'male'", 'max_length': '10'}),
            'voter_id': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '100'}),
            'voucher_no': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '100', 'blank': 'True'})
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
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'processed': ('django.db.models.fields.BooleanField', [], {'default': 'False'})
        },
        u'electoral_data.userprofile': {
            'Meta': {'object_name': 'UserProfile'},
            'assembly': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['electoral_data.AssemblyConstituency']", 'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'polling_station': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['electoral_data.PollingStation']", 'null': 'True', 'blank': 'True'}),
            'user': ('django.db.models.fields.related.OneToOneField', [], {'to': u"orm['auth.User']", 'unique': 'True'})
        }
    }

    complete_apps = ['electoral_data']