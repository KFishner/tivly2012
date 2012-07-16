# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Deleting model 'Apps'
        db.delete_table('Tivly_apps')

        # Deleting model 'UserApps'
        db.delete_table('Tivly_userapps')


        # Changing field 'Cards.typeString'
        db.alter_column('Tivly_cards', 'typeString', self.gf('django.db.models.fields.CharField')(max_length=20))
        # Deleting field 'Businesses.hours'
        db.delete_column('Tivly_businesses', 'hours')


        # Changing field 'Businesses.website'
        db.alter_column('Tivly_businesses', 'website', self.gf('django.db.models.fields.CharField')(max_length=50))

        # Changing field 'Businesses.city'
        db.alter_column('Tivly_businesses', 'city', self.gf('django.db.models.fields.CharField')(max_length=20))

        # Changing field 'Businesses.pictureLocation'
        db.alter_column('Tivly_businesses', 'pictureLocation', self.gf('django.db.models.fields.CharField')(max_length=50))

        # Changing field 'Businesses.street'
        db.alter_column('Tivly_businesses', 'street', self.gf('django.db.models.fields.CharField')(max_length=30))

        # Changing field 'Businesses.businessName'
        db.alter_column('Tivly_businesses', 'businessName', self.gf('django.db.models.fields.CharField')(max_length=20))
        # Deleting field 'MyRecommendations.recID'
        db.delete_column('Tivly_myrecommendations', 'recID')

        # Adding field 'MyRecommendations.rID'
        db.add_column('Tivly_myrecommendations', 'rID',
                      self.gf('django.db.models.fields.CharField')(default='void', max_length=6),
                      keep_default=False)


        # Changing field 'MyRecommendations.recommender'
        db.alter_column('Tivly_myrecommendations', 'recommender', self.gf('django.db.models.fields.CharField')(max_length=30))

    def backwards(self, orm):
        # Adding model 'Apps'
        db.create_table('Tivly_apps', (
            ('businessID', self.gf('django.db.models.fields.CharField')(max_length=40)),
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('appID', self.gf('django.db.models.fields.CharField')(max_length=40)),
        ))
        db.send_create_signal('Tivly', ['Apps'])

        # Adding model 'UserApps'
        db.create_table('Tivly_userapps', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('businessID', self.gf('django.db.models.fields.CharField')(max_length=40)),
            ('csID', self.gf('django.db.models.fields.CharField')(max_length=6)),
            ('appID', self.gf('django.db.models.fields.CharField')(max_length=40)),
        ))
        db.send_create_signal('Tivly', ['UserApps'])


        # Changing field 'Cards.typeString'
        db.alter_column('Tivly_cards', 'typeString', self.gf('django.db.models.fields.CharField')(max_length=10))
        # Adding field 'Businesses.hours'
        db.add_column('Tivly_businesses', 'hours',
                      self.gf('django.db.models.fields.CharField')(default='void', max_length=100),
                      keep_default=False)


        # Changing field 'Businesses.website'
        db.alter_column('Tivly_businesses', 'website', self.gf('django.db.models.fields.CharField')(max_length=100))

        # Changing field 'Businesses.city'
        db.alter_column('Tivly_businesses', 'city', self.gf('django.db.models.fields.CharField')(max_length=40))

        # Changing field 'Businesses.pictureLocation'
        db.alter_column('Tivly_businesses', 'pictureLocation', self.gf('django.db.models.fields.CharField')(max_length=100))

        # Changing field 'Businesses.street'
        db.alter_column('Tivly_businesses', 'street', self.gf('django.db.models.fields.CharField')(max_length=40))

        # Changing field 'Businesses.businessName'
        db.alter_column('Tivly_businesses', 'businessName', self.gf('django.db.models.fields.CharField')(max_length=50))
        # Adding field 'MyRecommendations.recID'
        db.add_column('Tivly_myrecommendations', 'recID',
                      self.gf('django.db.models.fields.CharField')(default='void', max_length=40),
                      keep_default=False)

        # Deleting field 'MyRecommendations.rID'
        db.delete_column('Tivly_myrecommendations', 'rID')


        # Changing field 'MyRecommendations.recommender'
        db.alter_column('Tivly_myrecommendations', 'recommender', self.gf('django.db.models.fields.CharField')(max_length=20))

    models = {
        'Tivly.businesses': {
            'Meta': {'object_name': 'Businesses'},
            'businessID': ('django.db.models.fields.CharField', [], {'max_length': '40'}),
            'businessName': ('django.db.models.fields.CharField', [], {'max_length': '20'}),
            'city': ('django.db.models.fields.CharField', [], {'max_length': '20'}),
            'description': ('django.db.models.fields.CharField', [], {'max_length': '400'}),
            'fridayHours': ('django.db.models.fields.CharField', [], {'max_length': '20'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'mondayHours': ('django.db.models.fields.CharField', [], {'max_length': '20'}),
            'pictureLocation': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'saturdayHours': ('django.db.models.fields.CharField', [], {'max_length': '20'}),
            'street': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            'sundayHours': ('django.db.models.fields.CharField', [], {'max_length': '20'}),
            'thursdayHours': ('django.db.models.fields.CharField', [], {'max_length': '20'}),
            'tuesdayHours': ('django.db.models.fields.CharField', [], {'max_length': '20'}),
            'website': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'wednesdayHours': ('django.db.models.fields.CharField', [], {'max_length': '20'}),
            'zipCode': ('django.db.models.fields.IntegerField', [], {})
        },
        'Tivly.cards': {
            'Meta': {'object_name': 'Cards'},
            'cardType': ('django.db.models.fields.CharField', [], {'max_length': '20'}),
            'csID': ('django.db.models.fields.CharField', [], {'max_length': '6'}),
            'expDate': ('django.db.models.fields.CharField', [], {'max_length': '20'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'last4': ('django.db.models.fields.IntegerField', [], {}),
            'token': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            'typeString': ('django.db.models.fields.CharField', [], {'max_length': '20'})
        },
        'Tivly.cardspringuser': {
            'Meta': {'object_name': 'CardSpringUser'},
            'TwitID': ('django.db.models.fields.BigIntegerField', [], {'null': 'True', 'blank': 'True'}),
            'csID': ('django.db.models.fields.CharField', [], {'max_length': '6'}),
            'fbID': ('django.db.models.fields.BigIntegerField', [], {'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'points': ('django.db.models.fields.IntegerField', [], {})
        },
        'Tivly.fbaccesstokens': {
            'Meta': {'object_name': 'FBAccessTokens'},
            'accessToken': ('django.db.models.fields.CharField', [], {'max_length': '300'}),
            'date_created': ('django.db.models.fields.DateField', [], {}),
            'expiration_accessToken': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['Tivly.FBUser']"})
        },
        'Tivly.fbfriends': {
            'Meta': {'object_name': 'FBFriends'},
            'friend_fb_id': ('django.db.models.fields.BigIntegerField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '300'}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['Tivly.FBUser']"})
        },
        'Tivly.fbuser': {
            'Meta': {'object_name': 'FBUser'},
            'date_joined': ('django.db.models.fields.DateField', [], {}),
            'email': ('django.db.models.fields.CharField', [], {'max_length': '40'}),
            'fb_id': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            'gender': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            'location': ('django.db.models.fields.CharField', [], {'max_length': '30'})
        },
        'Tivly.myrecommendations': {
            'Meta': {'object_name': 'MyRecommendations'},
            'appID': ('django.db.models.fields.CharField', [], {'max_length': '40'}),
            'csID': ('django.db.models.fields.CharField', [], {'max_length': '6'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'rID': ('django.db.models.fields.CharField', [], {'max_length': '6'}),
            'recommender': ('django.db.models.fields.CharField', [], {'max_length': '30'})
        },
        'Tivly.myrewards': {
            'Meta': {'object_name': 'MyRewards'},
            'csID': ('django.db.models.fields.CharField', [], {'max_length': '6'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'reward': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['Tivly.Rewards']", 'symmetrical': 'False'})
        },
        'Tivly.rewards': {
            'Active': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'Meta': {'object_name': 'Rewards'},
            'appID': ('django.db.models.fields.CharField', [], {'max_length': '40'}),
            'businessID': ('django.db.models.fields.CharField', [], {'max_length': '40'}),
            'description': ('django.db.models.fields.CharField', [], {'max_length': '300'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'pointsNeeded': ('django.db.models.fields.IntegerField', [], {}),
            'rID': ('django.db.models.fields.CharField', [], {'max_length': '6'})
        },
        'Tivly.transaction': {
            'Meta': {'object_name': 'Transaction'},
            'amount': ('django.db.models.fields.IntegerField', [], {}),
            'businessID': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            'card_token': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            'currency': ('django.db.models.fields.CharField', [], {'max_length': '5'}),
            'date': ('django.db.models.fields.DateField', [], {}),
            'event_type': ('django.db.models.fields.CharField', [], {'max_length': '20'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'store_id': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            'transaction_id': ('django.db.models.fields.CharField', [], {'max_length': '30'})
        },
        'Tivly.userpoints': {
            'Meta': {'object_name': 'UserPoints'},
            'businessID': ('django.db.models.fields.CharField', [], {'max_length': '40'}),
            'csID': ('django.db.models.fields.CharField', [], {'max_length': '6'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'points': ('django.db.models.fields.IntegerField', [], {})
        }
    }

    complete_apps = ['Tivly']