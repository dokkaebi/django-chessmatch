# Create your views here.
from djangorestframework import response, status, renderers, views
from restapi.forms import UserForm
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse
from resources import UserResource


class HTMLRenderer(renderers.BaseRenderer):
  """
   Basic renderer which just returns the content without any further serialization.
  """
  media_type = 'text/html'

class ListOrCreateUserView(views.ListOrCreateModelView):
  form=UserForm
  resource=UserResource

  def post(self, request):
    user = User.objects.create_user(self.CONTENT['username'], '', self.CONTENT['password'])
    return response.Response(status.HTTP_201_CREATED, headers={'Location': reverse('user_detail', args=[user.id])})

class UserDetailView(views.InstanceModelView):
  resource=UserResource

