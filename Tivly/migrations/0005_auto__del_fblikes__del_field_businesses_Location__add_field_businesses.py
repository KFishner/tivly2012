# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Deleting model 'FBLikes'
        db.delete_table('Tivly_fblikes')

        # Deleting field 'Businesses.Location'
        db.delete_column('Tivly_businesses', 'Location')

        # Adding field 'Businesses.city'
        db.add_column('Tivly_businesses', 'city',
                      self.gf('django.db.models.fields.CharField')(default='Palo Alto', max_length=40),
                      keep_default=False)

        # Adding field 'Businesses.street'
        db.add_column('Tivly_businesses', 'street',
                      self.gf('django.db.models.fields.CharField')(default='514 Alma st', max_length=40),
                      keep_default=False)

        # Adding field 'Businesses.zip'
        db.add_column('Tivly_businesses', 'zip',
                      self.gf('django.db.models.fields.IntegerField')(default=18102),
                      keep_default=False)

        # Adding field 'Businesses.mondayHours'
        db.add_column('Tivly_businesses', 'mondayHours',
                      self.gf('django.db.models.fields.CharField')(default='11:30am - 930pm', max_length=10),
                      keep_default=False)

        # Adding field 'Businesses.tuesdayHours'
        db.add_column('Tivly_businesses', 'tuesdayHours',
                      self.gf('django.db.models.fields.CharField')(default='11:30am - 930pm', max_length=10),
                      keep_default=False)

        # Adding field 'Businesses.wednesdayHours'
        db.add_column('Tivly_businesses', 'wednesdayHours',
                      self.gf('django.db.models.fields.CharField')(default='11:30am - 930pm', max_length=10),
                      keep_default=False)

        # Adding field 'Businesses.thursdayHours'
        db.add_column('Tivly_businesses', 'thursdayHours',
                      self.gf('django.db.models.fields.CharField')(default='11:30am - 930pm', max_length=10),
                      keep_default=False)

        # Adding field 'Businesses.fridayHours'
        db.add_column('Tivly_businesses', 'fridayHours',
                      self.gf('django.db.models.fields.CharField')(default='11:30am - 930pm', max_length=10),
                      keep_default=False)

        # Adding field 'Businesses.saturdayHours'
        db.add_column('Tivly_businesses', 'saturdayHours',
                      self.gf('django.db.models.fields.CharField')(default='11:30am - 930pm', max_length=10),
                      keep_default=False)

        # Adding field 'Businesses.sundayHours'
        db.add_column('Tivly_businesses', 'sundayHours',
                      self.gf('django.db.models.fields.CharField')(default='11:30am - 930pm', max_length=10),
                      keep_default=False)


    def backwards(self, orm):
        # Adding model 'FBLikes'
        db.create_table('Tivly_fblikes', (
            ('category', self.gf('django.db.models.fields.CharField')(max_length=30)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=300)),
            ('user', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['Tivly.FBUser'])),
            ('created_time', self.gf('django.db.models.fields.DateField')()),
            ('likeId', self.gf('django.db.models.fields.BigIntegerField')()),
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
        ))
        db.send_create_signal('Tivly', ['FBLikes'])

        # Adding field 'Businesses.Location'
        db.add_column('Tivly_businesses', 'Location',
                      self.gf('django.db.models.fields.CharField')(default='void', max_length=40),
                      keep_default=False)

        # Deleting field 'Businesses.city'
        db.delete_column('Tivly_businesses', 'city')

        # Deleting field 'Businesses.street'
        db.delete_column('Tivly_businesses', 'street')

        # Deleting field 'Businesses.zip'
        db.delete_column('Tivly_businesses', 'zip')

        # Deleting field 'Businesses.mondayHours'
        db.delete_column('Tivly_businesses', 'mondayHours')

        # Deleting field 'Businesses.tuesdayHours'
        db.delete_column('Tivly_businesses', 'tuesdayHours')

        # Deleting field 'Businesses.wednesdayHours'
        db.delete_column('Tivly_businesses', 'wednesdayHours')

        # Deleting field 'Businesses.thursdayHours'
        db.delete_column('Tivly_businesses', 'thursdayHours')

        # Deleting field 'Businesses.fridayHours'
        db.delete_column('Tivly_businesses', 'fridayHours')

        # Deleting field 'Businesses.saturdayHours'
        db.delete_column('Tivly_businesses', 'saturdayHours')

        # Deleting field 'Businesses.sundayHours'
        db.delete_column('Tivly_businesses', 'sundayHours')


    models = {
        'Tivly.apps': {
            'Meta': {'object_name': 'Apps'},
            'appID': ('django.db.models.fields.CharField', [], {'max_length': '40'}),
            'businessID': ('django.db.models.fields.CharField', [], {'max_length': '40'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        'Tivly.businesses': {
            'Meta': {'object_name': 'Businesses'},
            'businessID': ('django.db.models.fields.CharField', [], {'max_length': '40'}),
            'businessName': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'city': ('django.db.models.fields.CharField', [], {'max_length': '40'}),
            'description': ('django.db.models.fields.CharField', [], {'max_length': '400'}),
            'fridayHours': ('django.db.models.fields.CharField', [], {'max_length': '10'}),
            'hours': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'mondayHours': ('django.db.models.fields.CharField', [], {'max_length': '10'}),
            'pictureLocation': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'saturdayHours': ('django.db.models.fields.CharField', [], {'max_length': '10'}),
            'street': ('django.db.models.fields.CharField', [], {'max_length': '40'}),
            'sundayHours': ('django.db.models.fields.CharField', [], {'max_length': '10'}),
            'thursdayHours': ('django.db.models.fields.CharField', [], {'max_length': '10'}),
            'tuesdayHours': ('django.db.models.fields.CharField', [], {'max_length': '10'}),
            'website': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'wednesdayHours': ('django.db.models.fields.CharField', [], {'max_length': '10'}),
            'zip': ('django.db.models.fields.IntegerField', [], {})
        },
        'Tivly.cards': {
            'Meta': {'object_name': 'Cards'},
            'cardType': ('django.db.models.fields.CharField', [], {'max_length': '20'}),
            'csID': ('django.db.models.fields.CharField', [], {'max_length': '6'}),
            'expDate': ('django.db.models.fields.CharField', [], {'max_length': '20'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'last4': ('django.db.models.fields.IntegerField', [], {}),
            'token': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            'typeString': ('django.db.models.fields.CharField', [], {'max_length': '10'})
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
            'recID': ('django.db.models.fields.CharField', [], {'max_length': '40'}),
            'recommender': ('django.db.models.fields.CharField', [], {'max_length': '20'})
        },
        'Tivly.myrewards': {
            'Meta': {'object_name': 'MyRewards'},
            'csID': ('django.db.models.fields.CharField', [], {'max_length': '6'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'reward': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['Tivly.Rewards']", 'symmetrical': 'False'})
        },
        'Tivly.rewards': {
            'Meta': {'object_name': 'Rewards'},
            'businessID': ('django.db.models.fields.CharField', [], {'max_length': '40'}),
            'description': ('django.db.models.fields.CharField', [], {'max_length': '300'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'pointsNeeded': ('django.db.models.fields.IntegerField', [], {})
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
        'Tivly.userapps': {
            'Meta': {'object_name': 'UserApps'},
            'appID': ('django.db.models.fields.CharField', [], {'max_length': '40'}),
            'businessID': ('django.db.models.fields.CharField', [], {'max_length': '40'}),
            'csID': ('django.db.models.fields.CharField', [], {'max_length': '6'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
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