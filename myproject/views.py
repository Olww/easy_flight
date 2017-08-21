from django.shortcuts import render_to_response, redirect
from django.contrib import auth
from forms import SearchForm
from tickets.models import Tickets
from datetime import datetime

def index(request):
	user = request.user
	staff = user.is_staff
	args={}
	args['staff'] = staff
	args['username'] = user.username
	return render_to_response('index.html', args)

def about(request):
	user = request.user
	staff = user.is_staff
	args={}
	args['staff'] = staff
	args['username'] = user.username
	return render_to_response('about.html', args)

def alko(request):
	user = request.user
	staff = user.is_staff
	args={}
	args['staff'] = staff
	args['username'] = user.username
	return render_to_response('alko.html', args)

def contacts(request):
	user = request.user
	staff = user.is_staff
	args={}
	args['staff'] = staff
	args['username'] = user.username
	return render_to_response('contacts.html', args)

def links(request):
	user = request.user
	staff = user.is_staff
	args={}
	args['staff'] = staff
	args['username'] = user.username
	return render_to_response('links.html', args)

def lcb(request):
	user = request.user
	staff = user.is_staff
	args={}
	args['staff'] = staff
	args['username'] = user.username
  	tickets = Tickets.objects.filter(tickets_user = user, tickets_date__gte = datetime.now())
	args['tickets']= tickets
	return render_to_response('lcb.html', args)

def lcb_admin(request):
	user = request.user
	staff = user.is_staff
	args={}
	args['staff'] = staff
	args['username'] = user.username
	tickets = Tickets.objects.filter(tickets_user = user, tickets_date__gte = datetime.now())
	args['tickets']= tickets
	return render_to_response('lcb_admin.html', args)

def user_delete(request, ticket_id):
	user = request.user
	staff = user.is_staff
	args={}
	args['staff'] = staff
	args['username'] = user.username
	tickets = Tickets.objects.filter(tickets_user = user, tickets_date__gte = datetime.now())
	args['tickets']= tickets
	ticket = Tickets.objects.get(id = ticket_id)
	ticket.tickets_user = None
	ticket.save()
	if staff:
		return redirect('/lcb_admin', args)
	else:
		return redirect('/lcb/', args)
	#endif

def user_add(request, ticket_id):
	ticket = Tickets.objects.get(id = ticket_id)
	ticket.tickets_user = request.user
	ticket.save()
	return redirect('/find/')

def find(request):
	args = {}
	user = request.user
	staff = user.is_staff
	args['staff'] = staff
	args['username'] = user.username
	if request.method == 'POST':
		tto = request.POST.get('tickets_to')
		tfrom = request.POST.get('tickets_from')
		tdate = request.POST.get('tickets_date')
		m1=tdate.encode('utf-8')
		m2 = datetime.strptime(m1,'%d.%m.%Y')
		tickets = Tickets.objects.filter(tickets_to = tto, tickets_from = tfrom,tickets_date = m2, tickets_date__gte = datetime.now(), tickets_user = None)
		args['tickets']= tickets
		args['tdate'] = m1
		args['form'] = SearchForm
		return render_to_response('find.html', args)
	else:
		args['form'] = SearchForm
		return render_to_response('find.html', args)
