from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.template import loader

from django.contrib.auth import get_user_model
from django.contrib.auth import (authenticate, login, logout)

from .forms import UserLoginForm, UserRegisterForm
from mainapp.models import Image


from django.contrib import messages
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.forms import PasswordChangeForm
from django.utils.translation import ugettext as _


from django.contrib.sites.shortcuts import get_current_site
from django.utils.encoding import force_bytes, force_text
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.template.loader import render_to_string
from .tokens import account_activation_token
from django.contrib.auth.models import User
from django.core.mail import EmailMessage

# Create your views here.
User = get_user_model()



def login_view(request):
	next = request.GET.get('next')
	form = UserLoginForm(request.POST or None)

	if form.is_valid():
		email = form.cleaned_data.get('email')
		password = form.cleaned_data.get('password')
		user = authenticate(email=email, password=password)
		login(request, user)
		if next:
			return redirect(next)
		return redirect('/home/')

	context = {'form':form}
	return render(request, "login.html", context)


def register_view(request):
	if request.method == 'POST':
		form = UserRegisterForm(request.POST)
		if form.is_valid():
			user = form.save(commit=False)
			user.is_active = False
			password = form.cleaned_data.get('password')
			user.set_password(password)
			user.save()
			current_site = get_current_site(request)
			mail_subject = 'Activate your restaurant account'
			message = render_to_string('acc_active_email.html', {
				'user': user,
				'domain': current_site.domain,
				'uid':urlsafe_base64_encode(force_bytes(user.pk)),
				'token':account_activation_token.make_token(user),
			})
			to_email = form.cleaned_data.get('email')
			email = EmailMessage(mail_subject, message, to=[to_email])
			email.send()
			template = loader.get_template('registration.html')
			return HttpResponse(template.render())
	else:
		form = UserRegisterForm()

	return render(request, "signup.html", {'form':form})



def logout_view(request):
	logout(request)
	return redirect('/home/')



def change_password(request):
    if request.method == 'POST':
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)
            messages.success(request, _('Your password was successfully updated!'))
            return redirect('/manageprofile/')
        else:
            messages.error(request, _('Please correct the error below.'))
    else:
        form = PasswordChangeForm(request.user)
    qs = Image.objects.filter(user=request.user)
    context = {'form':form, 'objs':qs}
    return render(request, 'change_password.html', context)








def activate(request, uidb64, token):
    try:
        uid = force_text(urlsafe_base64_decode(uidb64))
        user = User.objects.get(pk=uid)
    except(TypeError, ValueError, OverflowError, User.DoesNotExist):
        user = None
    if user is not None and account_activation_token.check_token(user, token):
        user.is_active = True
        user.save()
        login(request, user)
        #return redirect('/home/')
        return HttpResponse('Thank you for your email confirmation. Now you can login to your account.')
    else:
        return HttpResponse('Activation link is invalid!')