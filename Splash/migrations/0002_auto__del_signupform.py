# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Deleting model 'SignUpForm'
        db.delete_table('Splash_signupform')


    def backwards(self, orm):
        # Adding model 'SignUpForm'
        db.create_table('Splash_signupform', (
            ('email', self.gf('django.db.models.fields.CharField')(max_length=60)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=40)),
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
        ))
        db.send_create_signal('Splash', ['SignUpForm'])


    models = {
        'Splash.contactusform': {
            'Meta': {'object_name': 'ContactUsForm'},
            'email': ('django.db.models.fields.CharField', [], {'max_length': '60'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'message': ('django.db.models.fields.CharField', [], {'max_length': '400'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '40'})
        },
        'Splash.merchantsignupform': {
            'Meta': {'object_name': 'MerchantSignUpForm'},
            'city': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            'email': ('django.db.models.fields.CharField', [], {'max_length': '60'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'message': ('django.db.models.fields.CharField', [], {'max_length': '400'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '40'}),
            'phone': ('django.db.models.fields.BigIntegerField', [], {}),
            'restaurantName': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'state': ('django.db.models.fields.CharField', [], {'max_length': '2'}),
            'street': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'zip': ('django.db.models.fields.IntegerField', [], {})
        }
    }

    complete_apps = ['Splash']