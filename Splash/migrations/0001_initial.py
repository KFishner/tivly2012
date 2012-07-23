# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'SignUpForm'
        db.create_table('Splash_signupform', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=40)),
            ('email', self.gf('django.db.models.fields.CharField')(max_length=60)),
        ))
        db.send_create_signal('Splash', ['SignUpForm'])

        # Adding model 'MerchantSignUpForm'
        db.create_table('Splash_merchantsignupform', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=40)),
            ('restaurantName', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('city', self.gf('django.db.models.fields.CharField')(max_length=30)),
            ('state', self.gf('django.db.models.fields.CharField')(max_length=2)),
            ('street', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('zip', self.gf('django.db.models.fields.IntegerField')()),
            ('email', self.gf('django.db.models.fields.CharField')(max_length=60)),
            ('phone', self.gf('django.db.models.fields.BigIntegerField')()),
            ('message', self.gf('django.db.models.fields.CharField')(max_length=400)),
        ))
        db.send_create_signal('Splash', ['MerchantSignUpForm'])

        # Adding model 'ContactUsForm'
        db.create_table('Splash_contactusform', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=40)),
            ('email', self.gf('django.db.models.fields.CharField')(max_length=60)),
            ('message', self.gf('django.db.models.fields.CharField')(max_length=400)),
        ))
        db.send_create_signal('Splash', ['ContactUsForm'])


    def backwards(self, orm):
        # Deleting model 'SignUpForm'
        db.delete_table('Splash_signupform')

        # Deleting model 'MerchantSignUpForm'
        db.delete_table('Splash_merchantsignupform')

        # Deleting model 'ContactUsForm'
        db.delete_table('Splash_contactusform')


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
        },
        'Splash.signupform': {
            'Meta': {'object_name': 'SignUpForm'},
            'email': ('django.db.models.fields.CharField', [], {'max_length': '60'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '40'})
        }
    }

    complete_apps = ['Splash']