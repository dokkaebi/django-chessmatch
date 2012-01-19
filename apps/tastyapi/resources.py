from tastypie import fields
from tastypie.resources import ModelResource
from chessmatch.models import *
from django.contrib.auth.models import User

class UserResource(ModelResource):
  class Meta:
    queryset=User.objects.all()
    excludes=['password',]

class PlayerResource(ModelResource):
  user = fields.ForeignKey(UserResource, 'user')
  class Meta:
    queryset=Player.objects.all()
    excludes=['twitter_access_token']

class PieceColorResource(ModelResource):
  class Meta:
    queryset=PieceColor.objects.all()

class BoardSetupResource(ModelResource):
  created_by = fields.ForeignKey(UserResource, 'created_by')
  updated_by = fields.ForeignKey(UserResource, 'updated_by')
  files = fields.ListField(attribute='files',readonly=True)
  class Meta:
    queryset=BoardSetup.objects.all()

class BoardSetupColorResource(ModelResource):
  boardsetup = fields.ForeignKey(BoardSetupResource, 'board_setup')
  color = fields.ForeignKey(PieceColorResource, 'color')
  class Meta:
    queryset=BoardSetupColor.objects.all()

class GameResource(ModelResource):
  num_players = fields.IntegerField(attribute='num_players',readonly=True)
  comma_players = fields.CharField(attribute='comma_players',readonly=True)
  class Meta:
    queryset=Game.objects.all()

###
#  POST/PUT
# new Player (+User)
# new Game
# make move
# add/remove player to game?
# delete player/game/etc?
# new colors?
# new BoardSetup

#  GET
# players
# game
# boardsetup
# gameplayers
# 
###