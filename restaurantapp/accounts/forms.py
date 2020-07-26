from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth import (authenticate, login)
from mainapp.models import Image


User = get_user_model()

class UserLoginForm(forms.Form):
	email = forms.EmailField()
	password = forms.CharField(widget=forms.PasswordInput)


	def clean(self, *args, **kwargs):

		email = self.cleaned_data.get('email')
		password = self.cleaned_data.get('password')

		if email and password:
			user = authenticate(email=email, password=password)

			if not user:
				raise forms.ValidationError('This user does not exist!')

			if not user.check_password(password):
				raise forms.ValidationError('password is incorrect!')

			if not user.is_active:
				raise forms.ValidationError('This user is inactive!')

		return super(UserLoginForm, self).clean(*args, **kwargs)


class UserRegisterForm(forms.ModelForm):

	email = forms.EmailField(label='Email Address')
	password = forms.CharField(widget=forms.PasswordInput)
	name = forms.CharField()

	class Meta:
		model = User
		fields = ['email', 'password', 'name']


	def clean_email(self):

		email = self.cleaned_data.get('email')
		email_qs = User.objects.filter(email=email)
		if email_qs.exists():
			raise forms.ValidationError('This email is in use!')

		return email




class ImageForm(forms.ModelForm):

	class Meta:
		model = Image
		fields = ['image']



		