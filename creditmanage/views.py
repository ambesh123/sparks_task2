from django.shortcuts import render
from .models import client

def home(request):
	return render(request , 'index.html')

def users(request):
	clients = client.objects.all()
	return render(request , 'users.html' , {'clients' : clients})