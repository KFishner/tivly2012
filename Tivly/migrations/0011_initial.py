# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'FBUser'
        db.create_table('Tivly_fbuser', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('first_name', self.gf('django.db.models.fields.CharField')(max_length=30)),
            ('last_name', self.gf('django.db.models.fields.CharField')(max_length=30)),
            ('email', self.gf('django.db.models.fields.CharField')(max_length=40)),
            ('gender', self.gf('django.db.models.fields.CharField')(max_length=30)),
            ('fb_id', self.gf('django.db.models.fields.CharField')(max_length=30)),
            ('location', self.gf('django.db.models.fields.CharField')(max_length=30)),
            ('date_joined', self.gf('django.db.models.fields.DateField')()),
        ))
        db.send_create_signal('Tivly', ['FBUser'])

        # Adding model 'FBAccessTokens'
        db.create_table('Tivly_fbaccesstokens', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('accessToken', self.gf('django.db.models.fields.CharField')(max_length=300)),
            ('expiration_accessToken', self.gf('django.db.models.fields.CharField')(max_length=30)),
            ('user', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['Tivly.FBUser'])),
            ('date_created', self.gf('django.db.models.fields.DateField')()),
        ))
        db.send_create_signal('Tivly', ['FBAccessTokens'])

        # Adding model 'FBFriends'
        db.create_table('Tivly_fbfriends', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=300)),
            ('friend_fb_id', self.gf('django.db.models.fields.BigIntegerField')()),
            ('user', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['Tivly.FBUser'])),
        ))
        db.send_create_signal('Tivly', ['FBFriends'])

        # Adding model 'Businesses'
        db.create_table('Tivly_businesses', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('businessID', self.gf('django.db.models.fields.CharField')(max_length=40)),
            ('businessName', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('city', self.gf('django.db.models.fields.CharField')(max_length=40)),
            ('street', self.gf('django.db.models.fields.CharField')(max_length=40)),
            ('zipCode', self.gf('django.db.models.fields.IntegerField')()),
            ('mondayHours', self.gf('django.db.models.fields.CharField')(max_length=20)),
            ('tuesdayHours', self.gf('django.db.models.fields.CharField')(max_length=20)),
            ('wednesdayHours', self.gf('django.db.models.fields.CharField')(max_length=20)),
            ('thursdayHours', self.gf('django.db.models.fields.CharField')(max_length=20)),
            ('fridayHours', self.gf('django.db.models.fields.CharField')(max_length=20)),
            ('saturdayHours', self.gf('django.db.models.fields.CharField')(max_length=20)),
            ('sundayHours', self.gf('django.db.models.fields.CharField')(max_length=20)),
            ('description', self.gf('django.db.models.fields.CharField')(max_length=400)),
            ('pictureLocation', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('website', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('hours', self.gf('django.db.models.fields.CharField')(max_length=100)),
        ))
        db.send_create_signal('Tivly', ['Businesses'])

        # Adding model 'Apps'
        db.create_table('Tivly_apps', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('appID', self.gf('django.db.models.fields.CharField')(max_length=40)),
            ('businessID', self.gf('django.db.models.fields.CharField')(max_length=40)),
        ))
        db.send_create_signal('Tivly', ['Apps'])

        # Adding model 'Rewards'
        db.create_table('Tivly_rewards', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('rID', self.gf('django.db.models.fields.CharField')(max_length=6)),
            ('businessID', self.gf('django.db.models.fields.CharField')(max_length=40)),
            ('description', self.gf('django.db.models.fields.CharField')(max_length=300)),
            ('Active', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('pointsNeeded', self.gf('django.db.models.fields.IntegerField')()),
        ))
        db.send_create_signal('Tivly', ['Rewards'])

        # Adding model 'CardSpringUser'
        db.create_table('Tivly_cardspringuser', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('csID', self.gf('django.db.models.fields.CharField')(max_length=6)),
            ('points', self.gf('django.db.models.fields.IntegerField')()),
            ('fbID', self.gf('django.db.models.fields.BigIntegerField')(null=True, blank=True)),
            ('TwitID', self.gf('django.db.models.fields.BigIntegerField')(null=True, blank=True)),
        ))
        db.send_create_signal('Tivly', ['CardSpringUser'])

        # Adding model 'Cards'
        db.create_table('Tivly_cards', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('csID', self.gf('django.db.models.fields.CharField')(max_length=6)),
            ('token', self.gf('django.db.models.fields.CharField')(max_length=30)),
            ('last4', self.gf('django.db.models.fields.IntegerField')()),
            ('expDate', self.gf('django.db.models.fields.CharField')(max_length=20)),
            ('cardType', self.gf('django.db.models.fields.CharField')(max_length=20)),
            ('typeString', self.gf('django.db.models.fields.CharField')(max_length=10)),
        ))
        db.send_create_signal('Tivly', ['Cards'])

        # Adding model 'UserPoints'
        db.create_table('Tivly_userpoints', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('csID', self.gf('django.db.models.fields.CharField')(max_length=6)),
            ('businessID', self.gf('django.db.models.fields.CharField')(max_length=40)),
            ('points', self.gf('django.db.models.fields.IntegerField')()),
        ))
        db.send_create_signal('Tivly', ['UserPoints'])

        # Adding model 'UserApps'
        db.create_table('Tivly_userapps', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('csID', self.gf('django.db.models.fields.CharField')(max_length=6)),
            ('appID', self.gf('django.db.models.fields.CharField')(max_length=40)),
            ('businessID', self.gf('django.db.models.fields.CharField')(max_length=40)),
        ))
        db.send_create_signal('Tivly', ['UserApps'])

        # Adding model 'MyRecommendations'
        db.create_table('Tivly_myrecommendations', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('csID', self.gf('django.db.models.fields.CharField')(max_length=6)),
            ('appID', self.gf('django.db.models.fields.CharField')(max_length=40)),
            ('recID', self.gf('django.db.models.fields.CharField')(max_length=40)),
            ('recommender', self.gf('django.db.models.fields.CharField')(max_length=20)),
        ))
        db.send_create_signal('Tivly', ['MyRecommendations'])

        # Adding model 'MyRewards'
        db.create_table('Tivly_myrewards', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('csID', self.gf('django.db.models.fields.CharField')(max_length=6)),
        ))
        db.send_create_signal('Tivly', ['MyRewards'])

        # Adding M2M table for field reward on 'MyRewards'
        db.create_table('Tivly_myrewards_reward', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('myrewards', models.ForeignKey(orm['Tivly.myrewards'], null=False)),
            ('rewards', models.ForeignKey(orm['Tivly.rewards'], null=False))
        ))
        db.create_unique('Tivly_myrewards_reward', ['myrewards_id', 'rewards_id'])

        # Adding model 'Transaction'
        db.create_table('Tivly_transaction', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('date', self.gf('django.db.models.fields.DateField')()),
            ('event_type', self.gf('django.db.models.fields.CharField')(max_length=20)),
            ('businessID', self.gf('django.db.models.fields.CharField')(max_length=30)),
            ('currency', self.gf('django.db.models.fields.CharField')(max_length=5)),
            ('amount', self.gf('django.db.models.fields.IntegerField')()),
            ('card_token', self.gf('django.db.models.fields.CharField')(max_length=30)),
            ('transaction_id', self.gf('django.db.models.fields.CharField')(max_length=30)),
            ('store_id', self.gf('django.db.models.fields.CharField')(max_length=30)),
        ))
        db.send_create_signal('Tivly', ['Transaction'])


    def backwards(self, orm):
        # Deleting model 'FBUser'
        db.delete_table('Tivly_fbuser')

        # Deleting model 'FBAccessTokens'
        db.delete_table('Tivly_fbaccesstokens')

        # Deleting model 'FBFriends'
        db.delete_table('Tivly_fbfriends')

        # Deleting model 'Businesses'
        db.delete_table('Tivly_businesses')

        # Deleting model 'Apps'
        db.delete_table('Tivly_apps')

        # Deleting model 'Rewards'
        db.delete_table('Tivly_rewards')

        # Deleting model 'CardSpringUser'
        db.delete_table('Tivly_cardspringuser')

        # Deleting model 'Cards'
        db.delete_table('Tivly_cards')

        # Deleting model 'UserPoints'
        db.delete_table('Tivly_userpoints')

        # Deleting model 'UserApps'
        db.delete_table('Tivly_userapps')

        # Deleting model 'MyRecommendations'
        db.delete_table('Tivly_myrecommendations')

        # Deleting model 'MyRewards'
        db.delete_table('Tivly_myrewards')

        # Removing M2M table for field reward on 'MyRewards'
        db.delete_table('Tivly_myrewards_reward')

        # Deleting model 'Transaction'
        db.delete_table('Tivly_transaction')


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
            'fridayHours': ('django.db.models.fields.CharField', [], {'max_length': '20'}),
            'hours': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'mondayHours': ('django.db.models.fields.CharField', [], {'max_length': '20'}),
            'pictureLocation': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'saturdayHours': ('django.db.models.fields.CharField', [], {'max_length': '20'}),
            'street': ('django.db.models.fields.CharField', [], {'max_length': '40'}),
            'sundayHours': ('django.db.models.fields.CharField', [], {'max_length': '20'}),
            'thursdayHours': ('django.db.models.fields.CharField', [], {'max_length': '20'}),
            'tuesdayHours': ('django.db.models.fields.CharField', [], {'max_length': '20'}),
            'website': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
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
            'Active': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'Meta': {'object_name': 'Rewards'},
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