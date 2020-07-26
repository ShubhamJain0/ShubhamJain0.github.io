from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.http import JsonResponse
from django.core import serializers
from .models import (orderfood, yourorder, cartitems, manageaddress, addressid, search, Order, Image,  BookingTable)
from datetime import date
from mainapp.forms import (addressform, ContactForm,  BookTable)
from accounts.forms import ImageForm

from django.core.mail import send_mail

from django.db.models import (Sum, Count)

@login_required
def homepage(request):
	qs = Image.objects.filter(user=request.user)
	context = {'objs':qs}
	return render(request, "home.html", context)



@login_required
def orderpage(request):

	qs = orderfood.objects.all()
	qus = cartitems.objects.filter(user=request.user).values('ordereditems').annotate(cou=Count('ordereditems'))
	breakfast_qs = orderfood.objects.filter(category="BreakFast")
	lunch_qs = orderfood.objects.filter(category="Lunch")
	dinner_qs = orderfood.objects.filter(category="Dinner")
	image_qs = Image.objects.filter(user=request.user)
	context = {'object_list':qs, 'objecs':qus, 'breakfastobj':breakfast_qs, 'lunchobj':lunch_qs, 'dinnerobj': dinner_qs, 
				'objs':image_qs}
	return render(request, "order.html", context)



@login_required
def cartpage(request):
	if request.method == 'POST' and request.is_ajax():
		ids = request.POST['ids']
		item = orderfood.objects.filter(id=ids).values_list('items', flat=True) 
		for i in item:
			new_item = i
		get_price = orderfood.objects.filter(id=ids).values_list('price', flat=True)
		for i in get_price:
			price = i
		cartitems.objects.create(ordereditems=new_item, price=price, user=request.user)
	qs = cartitems.objects.filter(user=request.user)
	context = {'objects':qs}
	return redirect('/order/')









@login_required
def cartforsearch(request):

	if request.method == 'POST':
		ids = request.POST.get('ids')
		item = orderfood.objects.filter(id=ids).values_list('items', flat=True) 
		for i in item:
			new_item = i
		get_price = orderfood.objects.filter(id=ids).values_list('price', flat=True)
		for i in get_price:
			price = i
		cartitems.objects.create(ordereditems=new_item, price=price, user=request.user)
	return redirect('/order/')



@login_required
def cancelitem(request):
	if request.method == 'POST':
		item = request.POST['items']
		cartitems.objects.filter(ordereditems=item, user=request.user).delete()
	return redirect('/order/')
	




@login_required
def deletecartpage(request):
	qs = cartitems.objects.filter(user=request.user)
	if request.method == 'POST':
		qs.delete()
		return redirect('/order/')
	context = {'objects':qs}
	return render(request, "delete.html", context)



@login_required
def confirmorder(request):
	
	if request.method == 'POST':
		addressid.objects.filter(user=request.user).delete()
		new_id = request.POST.get('select')
		addressid.objects.create(addressidofuser=new_id, user=request.user)
		return redirect('/order/')
	image_qs = Image.objects.filter(user=request.user)
	qs = cartitems.objects.filter(user=request.user).values('ordereditems', 'price').annotate(cou=Count('ordereddate'), c=Sum('price'))
	enable = False
	if qs:
		enable = True
	get_id = addressid.objects.filter(user=request.user).values_list('addressidofuser', flat=True)
	objects = manageaddress.objects.filter(id__in=get_id, user=request.user)
	addresss = False
	if objects:
		addresss = True
	total_price = cartitems.objects.filter(user=request.user).aggregate(Sum('price'))

	if total_price['price__sum'] is None:
		grand_total_price = 0
		total_price['price__sum'] = 0
	else:
		grand_total_price =  total_price['price__sum'] + 10 + 25 - 10

	context = {'object_list':qs, 'objects':objects, 'total_price':total_price, 'grand_total_price':grand_total_price, 'enable':enable,
				'objs':image_qs, 'addresss':addresss}
	return render(request, "confirm.html", context)



@login_required
def manageaddressview(request):
	form = addressform(request.POST or None)
	if form.is_valid():
		print(form.cleaned_data)
		form = form.save(commit=False)
		form.user = request.user
		form.save()
		form = addressform()
	qs = manageaddress.objects.filter(user=request.user)
	image_qs = Image.objects.filter(user=request.user)
	context = {'form':form, 'object_list':qs, 'objs':image_qs}
	return render(request,"address.html", context)



@login_required
def finalcancelview(request):
	if request.method == 'POST':
		item = request.POST.get('items')
		cartitems.objects.filter(ordereditems=item, user=request.user).delete()
	return redirect('/confirm/')
	




@login_required
def placeorder(request):
	items = cartitems.objects.filter(user=request.user)
	get_id = addressid.objects.filter(user=request.user).values_list('addressidofuser', flat=True)
	ids =  manageaddress.objects.filter(id__in=get_id, user=request.user)
	price = cartitems.objects.aggregate(Sum('price'))
	total_price =  price['price__sum'] + 10 + 25 - 10
	for i in ids:
		houseno = i.houseno
		street = i.street
		locality = i.locality
		city = i.city
		phoneno = i.phone
	for i in items:
		item = i.ordereditems
		yourorder.objects.create(ordereditems=item, user=request.user, houseno=houseno, street=street, locality=locality, 
			city=city, phone=phoneno)
		Order.objects.create(ordereditems=item, user=request.user, houseno=houseno, street=street, locality=locality, 
			city=city, phone=phoneno, price=total_price)
	
	return redirect('/finaltemplate/')



@login_required
def yourorders(request):

	qs = yourorder.objects.filter(user=request.user)
	qs2 = yourorder.objects.filter(user=request.user).values('ordereditems', 'ordereddate').annotate(cou=Count('ordereditems'))
	image_qs = Image.objects.filter(user=request.user)
	context = {'objects':qs, 'ob':qs2, 'objs':image_qs}
	return render(request, "yourorder.html", context)


@login_required
def repeatorder(request):

	if request.method == 'POST':
		item = request.POST.get('items')
		get_price = orderfood.objects.filter(items=item).values_list('price', flat=True)
		for i in get_price:
			price = i
		cartitems.objects.create(ordereditems=item, price=price, user=request.user)
		return redirect('/order/')




@login_required
def deletepreviousorderview(request):
	if request.method == 'POST':
		item = request.POST.get('items')
		get_date = yourorder.objects.filter(ordereditems=item).values_list('ordereddate', flat=True)
		for i in get_date:
			date = i
		yourorder.objects.filter(ordereditems=item, ordereddate=date , user=request.user).delete()
		return redirect('/yourorders/')




@login_required
def deleteallordersview(request):

	yourorder.objects.filter(user=request.user).delete()
	return redirect('/yourorders/')




@login_required
def manageprofilepage(request):
	form= ImageForm(request.POST or None, request.FILES or None)
	if form.is_valid():
		Image.objects.filter(user=request.user).delete()
		form = form.save(commit=False)
		form.user = request.user
		form.save()
		form = ImageForm()
	qs = Image.objects.filter(user=request.user)
	image_qs = Image.objects.filter(user=request.user)
	context = {'form':form, 'objects':qs, 'objs':image_qs}
	return render(request, "manageprofile.html", context)



@login_required
def deleteaddressview(request):

	if request.method == 'POST':
		deleteaddress = request.POST.get('delete')
		manageaddress.objects.filter(id=deleteaddress, user=request.user).delete()
		return redirect('/address/')
		


@login_required
def Searching(request):
	query=request.GET.get('q', None)
	qs = Image.objects.filter(user=request.user)
	
	if request.user.is_authenticated:
		user=request.user
	context={"query":query}
	if query is not None:
		search.objects.create(user=user, query=query)
		item_list=orderfood.objects.search(query=query)
		context['item_list']=item_list
		context['objs']=qs
	return render(request, 'search.html', context)



@login_required
def carthtml(request):

	qs = cartitems.objects.filter(user=request.user).values('ordereditems').annotate(cou=Count('ordereddate'))
	context = {'objects':qs}
	return render(request, 'cart.html', context)



@login_required
def LocationView(request):
	qs = Image.objects.filter(user=request.user)
	context = {'objs':qs}
	return render(request, 'location.html', context)


@login_required
def finaltemplateview(request):
	qs = Image.objects.filter(user=request.user)
	context = {'objs':qs}
	return render(request, "placeorder.html", context)



@login_required
def reduceitemview(request):

	if request.method == 'POST'  and request.is_ajax():
		item = request.POST['items']
		cartitems.objects.filter(pk__in=cartitems.objects.filter(ordereditems=item, user=request.user).\
			values_list('id', flat=True)[0:1]).delete()
	return redirect('/order/')
	


@login_required
def navbarimage(request):

	qs = Image.objects.filter(user=request.user)
	context = {'objs':qs}
	return render(request, 'navbar.html', context)



@login_required
def contactpageform(request):

	success = None
	if request.method == 'POST':
		form = ContactForm(request.POST or None)
		if form.is_valid():
			message = form.cleaned_data['message']
			from_email = form.cleaned_data['email']
			name = form.cleaned_data['name']
			send_mail(name, message, from_email, ['kotechashubham94@gmail.com'])
			success = True
			form = ContactForm()
	else:
		form = ContactForm()
	qs = Image.objects.filter(user=request.user)
	context = {'objs':qs, 'form':form, 'success':success}
	return render(request, 'contact.html', context)



@login_required
def booktableview(request):

	if request.method == 'POST':
		form = BookTable(request.POST or None)
		if form.is_valid():
			BookingTable.objects.filter(user=request.user).delete()
			form = form.save(commit=False)
			form.user = request.user
			form.save()
			form = BookTable()
	else:
		form = BookTable()
	qs = Image.objects.filter(user=request.user)
	context = {'form':form, 'objs':qs}
	return render(request, 'booktable.html', context)



@login_required
def Bookingslist(request):

	qs = BookingTable.objects.filter(user=request.user)
	qs2 = Image.objects.filter(user=request.user)
	context = {'objects':qs, 'objs':qs2}
	return render(request, 'Bookingslist.html', context)