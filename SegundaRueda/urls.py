"""SegundaRueda URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls import url, include
from django.contrib import admin
from SeRu.views import *
from django.views.generic import TemplateView
from SeRu.models import *
from rest_framework import routers, serializers, viewsets
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.permissions import IsAuthenticated
#from django_openid_auth import *

app_name = 'SeRu'


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('username', 'telefono_contacto','first_name','last_name','email')

class PostSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Post
        fields = '__all__'

class VehiculoSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Vehiculo
        fields = '__all__'


class UserViewSet(viewsets.ModelViewSet):
    authentication_classes = (SessionAuthentication, BasicAuthentication,)
    permission_classes = (IsAuthenticated,)
    queryset = User.objects.all()
    serializer_class = UserSerializer

class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

class VehiculoViewSet(viewsets.ModelViewSet):
    authentication_classes = (SessionAuthentication, BasicAuthentication,)
    permission_classes = (IsAuthenticated,)
    queryset = Vehiculo.objects.all()
    serializer_class = VehiculoSerializer

router = routers.DefaultRouter()
router.register(r'APIusuarios', UserViewSet)
router.register(r'APIposts', PostViewSet)
router.register(r'APIvehiculos', VehiculoViewSet)

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^cuentas/', include('allauth.urls')),
    url(r'^openid/', include('django_openid_auth.urls')),
    url(r'^api/', include(router.urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    url(r'^accounts/', include('django.contrib.auth.urls')),
    url(r'^$',TemplateView.as_view(template_name='SeRu/home.html')),
    url(r'^registrarse/$', Registrarse, name='registrarse'),
    url(r'^usuarios/$',ListaUsers.as_view(), name='usuarios'),
    url(r'^usuarios/borrar/(?P<pk>[0-9]+)/$',BorraPerfil.as_view(),name='borrar_usuario'),
    url(r'^usuarios/mostrar/(?P<pk>[0-9]+)/$',MuestraUsuario.as_view(), name='mostrar_usuario'),
    url(r'^posts/$', ListaPosts.as_view(), name='posts'),
#    url(r'^posts/agregar/$',CreaPost,name='nuevo_post'),
    url(r'^posts/agregar/$',CreaPost.as_view(),name='nuevo_post'),
    url(r'^posts/mostrar/(?P<pk>[0-9]+)/$',MuestraPost.as_view(),name='mostrar_post'),
#    url(r'^posts/modificar/(?P<pk>[0-9]+)/$',ActualizaPost.as_view(),name='cambiar_post'),
#    url(r'^posts/borrar/(?P<pk>[0-9]+)/$',BorraPost.as_view(),name='borrar_post'),
    url(r'^vehiculos/$', ListaVehiculos.as_view(), name='vehiculos'),
    url(r'^vehiculos/agregar/$',CreaVehiculo.as_view(),name='nuevo_vehiculo'),
#    url(r'^vehiculos/cambiar/(?P<pk>[0-9]+)/$',ActualizaVehiculo.as_view(),name='cambiar_post'),
    url(r'^vehiculos/mostrar/(?P<pk>[0-9]+)/$',MuestraVehiculo.as_view(),name='mostrar_vehiculo'),
#    url(r'^vehiculos/borrar/(?P<pk>[0-9]+)/$',BorraVehiculo.as_view(),name='borrar_vehiculo'),
]

if settings.DEBUG:
	urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
