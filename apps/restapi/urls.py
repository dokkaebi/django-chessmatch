from django.conf.urls.defaults import patterns, include, url
from django.conf import settings
from django.contrib import admin
from djangorestframework.views import ListOrCreateModelView, InstanceModelView
from restapi.resources import *

from views import ListOrCreateUserView

handler500 = 'mainsite.views.error500'
handler404 = 'mainsite.views.error404'


urlpatterns = patterns('',

    url(r'^player/$', ListOrCreateModelView.as_view(resource=PlayerResource), name='player_list'),
    url(r'^player/(?P<player_id>[0-9]+)/$', InstanceModelView.as_view(resource=PlayerResource)),

    url(r'^user/$', ListOrCreateUserView.as_view(), name='user_list'),
    url(r'^user/(?P<id>[0-9]+)/$', InstanceModelView.as_view(resource=UserResource), name='user_detail'),

    url(r'^pieceColor/$', ListOrCreateModelView.as_view(resource=PieceColorResource), name='pieceColor_list'),
    url(r'^pieceColor/(?P<id>[0-9]+)/$', InstanceModelView.as_view(resource=PieceColorResource), name='pieceColor_detail'),

    url(r'^boardSetup/$', ListOrCreateModelView.as_view(resource=BoardSetupResource), name='boardSetup_list'),
    url(r'^boardSetup/(?P<id>[0-9]+)/$', InstanceModelView.as_view(resource=BoardSetupResource), name='boardSetup_detail'),

    url(r'^boardSetupColor/$', ListOrCreateModelView.as_view(resource=BoardSetupColorResource), name='boardSetupColor_list'),
    url(r'^boardSetupColor/(?P<id>[0-9]+)/$', InstanceModelView.as_view(resource=BoardSetupColorResource), name='boardSetupColor_detail'),

    url(r'^game/$', ListOrCreateModelView.as_view(resource=GameResource), name='game_list'),
    url(r'^game/(?P<id>[0-9]+)/$', InstanceModelView.as_view(resource=GameResource), name='game_detail'),

    url(r'^gamePlayer/$', ListOrCreateModelView.as_view(resource=GamePlayerResource), name='gamePlayer_list'),
    url(r'^gamePlayer/(?P<id>[0-9]+)/$', InstanceModelView.as_view(resource=GamePlayerResource), name='gamePlayer_detail'),

    url(r'^gameAction/$', ListOrCreateModelView.as_view(resource=GameActionResource), name='gameAction_list'),
    url(r'^gameAction/(?P<id>[0-9]+)/$', InstanceModelView.as_view(resource=GameActionResource), name='gameAction_detail'),
)

if getattr(settings, 'DEBUG', False) or getattr(settings, 'DEBUG_STATIC', False):
    # If we are in debug mode, prepend a rule to urlpatterns to serve the static media
    import re
    urlpatterns = patterns('',
        url(r'^%s(?P<path>.*)$' % re.escape(settings.STATIC_URL), 'django.views.static.serve', {
            'document_root': settings.STATIC_ROOT
        }),
    ) + urlpatterns
