from djangorestframework.resources import ModelResource 
from chessmatch.models import *

from django.contrib.auth.models import User

class UserResource(ModelResource):
  model=User
  exclude=['password']

class PlayerResource(ModelResource):
  model=Player
  excludes = ['twitter_access_token']
  merges = {'user':UserResource}
#replace fields specified in merges
  fields=[(f.name, merges[f.name]) if f.name in merges else f.name for f in model._meta.fields]
#remove excluded fields
  fields[:] = [f for f in fields if f not in excludes]

class PieceColorResource(ModelResource):
  model=PieceColor

class BoardSetupResource(ModelResource):
  model=BoardSetup
  merges={'created_by':UserResource, 'updated_by': UserResource}
  includes=['files']
#replace fields specified in merges
  fields=[(f.name, merges[f.name]) if f.name in merges else f.name for f in model._meta.fields]
  fields += includes

class BoardSetupColorResource(ModelResource):
  model=BoardSetupColor
  merges={'board_setup':BoardSetupResource, 'color': PieceColorResource}
#replace fields specified in merges
  fields=[(f.name, merges[f.name]) if f.name in merges else f.name for f in model._meta.fields]

class GameResource(ModelResource):
  model=Game
  includes=['num_players','comma_players']
  merges={'board_setup':BoardSetupResource,
    'created_by': UserResource,
    'updated_by': UserResource,
  #  'winner': GamePlayerResource,
  }
#replace fields specified in merges
  fields=[(f.name, merges[f.name]) if f.name in merges else f.name for f in model._meta.fields]
  fields += includes

class GamePlayerResource(ModelResource):
  model=GamePlayer
  merges={'game': GameResource, 'player': PlayerResource, 'color': PieceColorResource, 'controller': 'self'}
  includes=[('controlling_player', PlayerResource)]
#replace fields specified in merges
  fields=[(f.name, merges[f.name]) if f.name in merges else f.name for f in model._meta.fields]
  fields += includes

class GameActionResource(ModelResource):
  model=GameAction
  merges={'game': GameResource}
  includes=['expression']

