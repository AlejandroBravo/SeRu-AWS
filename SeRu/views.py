# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.views.generic.detail import DetailView
from django.urls import reverse_lazy
from .models import Vehiculo, Post, User
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect
from .forms import *
from django.http import HttpResponseRedirect,HttpResponse
from django.contrib.auth.decorators import login_required
# Create your views here.

class ListaUsers(ListView):
	model = User
	template_name = 'SeRu/usuarios.html'

class ListaPosts(ListView):
	model = Post
	template_name='SeRu/posts.html'

class ListaVehiculos(ListView):
	model = Vehiculo
	template_name='SeRu/vehiculos.html'

class MuestraPost(DetailView):
	model = Post
	fields = '__all__'
	template_name='SeRu/mostrar_post.html'

class MuestraVehiculo(DetailView):
	model = Vehiculo
	fields = '__all__'
	template_name='SeRu/mostrar_vehiculo.html'

class MuestraUsuario(DetailView):
	model = User
	fields = '__all__'
	template_name='SeRu/mostrar_usuario.html'

class CreaPerfil(CreateView):
	model = User
	fields = '__all__'
	success_url = reverse_lazy('usuarios')
	template_name='SeRu/nuevo_usuario.html'

class ActualizaPerfil(UpdateView):
	model = User
	fields = '__all__'
	success_url = reverse_lazy('usuarios')
	template_name='SeRu/cambiar_usuario.html'

class BorraPerfil(DeleteView):
	model = User
	fields = '__all__'
	success_url = reverse_lazy('usuarios')
	template_name='SeRu/borrar_usuario.html'

class CreaVehiculo(CreateView):
	model = Vehiculo
	fields = '__all__'
	success_url = reverse_lazy('vehiculos')
	template_name='SeRu/nuevo_vehiculo.html'

class ActualizaVehiculo(UpdateView):
	model = Vehiculo
	fields = '__all__'
	success_url = reverse_lazy('vehiculos')
	template_name='SeRu/cambiar_vehiculo.html'

class BorraVehiculo(DeleteView):
	model = Vehiculo
	fields = '__all__'
	success_url = reverse_lazy('vehiculos')
	template_name='SeRu/borrar_vehiculo.html'

class CreaPost(CreateView):
	model = Post
	fields = '__all__'
	success_url = reverse_lazy('posts')
	template_name='SeRu/nuevo_post.html'

#def CreaPost(request):
#	if request.method == 'POST':
#		form1 = FormCreaPost(request.POST)
#		if form1.is_valid():
#			usuario = User.objects.get(user=request.user)
#			post.usuario_creador = usuario
#			post.nombre_post = form1.cleaned_data.get('nombre_post')
#			post.vehiculo_id = form1.cleaned_data.get('vehiculo_id')
#			post.ubicacion = form1.cleaned_data.get('ubicacion')
#			post.descripcion = form1.cleaned_data.get('descripcion')
#			post.precio = form1.cleaned_data.get('precio')
#			post.save()
			#return HttpResponseRedirect('/posts/')
#	else:
#		form1 = FormCreaPost()
#	return render(request,'SeRu/nuevo_post.html',{'post':form1})
	
class ActualizaPost(UpdateView):
	model = Post
	fields = '__all__'
	success_url = reverse_lazy('posts')
	template_name='SeRu/cambiar_post.html'

class BorraPost(DeleteView):
	model = Post
	fields = '__all__'
	success_url = reverse_lazy('posts')
	template_name='SeRu/borrar_post.html'

def Registrarse(request):
	if request.method == 'POST':
		form = UserCreateForm(request.POST)
		if form.is_valid():
			form.save()
			return redirect('/')
	else:
		form = UserCreateForm()
	return render(request, 'SeRu/registrarse.html', {'form': form})