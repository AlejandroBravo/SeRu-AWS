# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Vehiculo, Post, User
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect
from .forms import UserCreateForm
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
	
	def form_valid(self, form):
		form.instance.created_by = self.request.user
		return super('usuario_creador', self).form_valid(form)


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
			return redirect('usuarios')
	else:
		form = UserCreateForm()
	return render(request, 'SeRu/registrarse.html', {'form': form})