from django.shortcuts import render , HttpResponse , redirect
from .models import client

def home(request):
	return render(request , 'index.html')

def users(request):
	clients = client.objects.all()
	return render(request , 'users.html' , {'clients' : clients})

def choose_sender(request):
	clients = client.objects.all()
	return render(request , 'choose_sender.html' , {'clients' : clients})

def choose_receiver(request):
	sender = request.GET.get('sender')
	clients = client.objects.exclude(uid = sender)
	if sender == None:
		return(HttpResponse("<h1>Invalid Request</h1>"))
	request.session['sender'] = sender
	return render(request, 'choose_receiver.html' , {'clients' : clients , 'sender' : sender})

def enter_amount(request):
	receiver = request.GET.get('receiver')
	if receiver == None:
		return(HttpResponse("<h1>Invalid Request</h1>"))
	request.session['receiver'] = receiver
	return render(request, 'enter_amount.html')

def set_amount(request):
	amount = request.GET.get('amount')
	if amount == None:
		return(HttpResponse("<h1>Invalid Request</h1>"))
	request.session['amount'] = amount
	return HttpResponse("<center><button class = 'btn btn-lg btn-danger' onclick = 'finalize()'>Confirm</button></center>")

def transfer(request):
	return render(request , 'transfer.html')

def finalize(request):
	sender_id = request.session['sender']
	receiver_id = request.session['receiver']
	amount = request.session['amount']

	if sender_id == None or receiver_id == None or amount == None :
		return HttpResponse("Bad Request")

	sender = client.objects.get(uid = sender_id)
	receiver = client.objects.get(uid = receiver_id)
	amount = int(amount)

	sender.deductMoney(amount)
	receiver.addMoney(amount)

	sender.save()
	receiver.save()

	return redirect('/')