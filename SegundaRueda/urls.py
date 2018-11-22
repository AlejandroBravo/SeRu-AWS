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
from django.conf.urls import url, include
from django.contrib import admin
from SeRu.views import *
from django.views.generic import TemplateView

app_name = 'SeRu'

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^accounts/', include('django.contrib.auth.urls')),
    url(r'^$',TemplateView.as_view(template_name='SeRu/home.html')),
    url(r'^registrarse/$', Registrarse, name='registrarse'),
    url(r'^usuarios/$',ListaUsers.as_view(), name='usuarios'),
    url(r'^posts/$', ListaPosts.as_view(), name='posts'),
    url(r'^posts/agregar/$',CreaPost.as_view(),name='nuevo_post'),
    url(r'^posts/mostrar/(?P<pk>[0-9]+)/$',MuestraPost.as_view(),name='mostrar_post'),
    url(r'^posts/modificar/(?P<pk>[0-9]+)/$',ActualizaPost.as_view(),name='cambiar_post'),
    url(r'^posts/borrar/(?P<pk>[0-9]+)/$',BorraPost.as_view(),name='borrar_post'),
    url(r'^vehiculos/$', ListaVehiculos.as_view(), name='vehiculos'),
    url(r'^vehiculos/agregar/$',CreaVehiculo.as_view(),name='nuevo_vehiculo'),
    url(r'^vehiculos/cambiar/(?P<pk>[0-9]+)/$',ActualizaVehiculo.as_view(),name='cambiar_post'),
    url(r'^vehiculos/borrar/(?P<pk>[0-9]+)/$',BorraVehiculo.as_view(),name='borrar_vehiculo'),
]
