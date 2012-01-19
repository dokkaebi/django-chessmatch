
from django.conf.urls.defaults import patterns, include, url
from django.conf import settings
from django.contrib import admin
from tastyapi.resources import *
from tastypie.api import Api


handler500 = 'mainsite.views.error500'
handler404 = 'mainsite.views.error404'

v1_api = Api(api_name='v1')
v1_api.register(UserResource())
v1_api.register(PlayerResource())
v1_api.register(PieceColorResource())
v1_api.register(BoardSetupResource())
v1_api.register(BoardSetupColorResource())
v1_api.register(GameResource())

urlpatterns = patterns('',

    url(r'', include(v1_api.urls)),

)

if getattr(settings, 'DEBUG', False) or getattr(settings, 'DEBUG_STATIC', False):
    # If we are in debug mode, prepend a rule to urlpatterns to serve the static media
    import re
    urlpatterns = patterns('',
        url(r'^%s(?P<path>.*)$' % re.escape(settings.STATIC_URL), 'django.views.static.serve', {
            'document_root': settings.STATIC_ROOT
        }),
    ) + urlpatterns
