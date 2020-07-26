from django import forms
from mainapp.models import (manageaddress, BookingTable)


class addressform(forms.ModelForm):

	houseno = forms.CharField(widget=forms.TextInput(attrs={'id': 'name',  'class':'input-text js-input'}))
	street = forms.IntegerField(widget=forms.TextInput(attrs={'id':'name', 'class':'input-text js-input'}))
	locality = forms.CharField(widget=forms.TextInput(attrs={'id':'name', 'class':'input-text js-input'}))
	city = forms.CharField(widget=forms.TextInput(attrs={'readonly':'readonly', 'id':'name', 'class':'input-text js-input'}), 
		initial='Hyderabad')
	phone = forms.CharField(min_length=10, widget=forms.TextInput(attrs={'id':'name', 'class':'input-text js-input'}))

	class Meta:
		model = manageaddress
		fields = ['id', 'houseno', 'street', 'locality', 'phone']




		def clean(self):

			phone=self.cleaned_data.get('phone')
			qs=manageaddress.objects.filter(phone=phone)
			if qs.exists():
				raise forms.ValidationError("Phone already in use")
			return phone



class ContactForm(forms.Form):

	message = forms.CharField(widget= forms.Textarea(attrs={'class':'form-control', 'id':'name'}))
	name = forms.CharField( widget=forms.TextInput(attrs={'class':'form-control', 'id':'name'}))
	email = forms.EmailField( widget=forms.TextInput(attrs={'class':'form-control', 'id':'name'}))




class BookTable(forms.ModelForm):

	class Meta:

		model = BookingTable
		fields = ['id', 'name', 'email', 'phone', 'persons', 'date', 'time']
		PERSON_CATEGORY = (

			('', 'Persons'),
			('1','1'),
			('2', '2'),
			('3','3'),
			('4','4'),
			('6','6'),
			('8','8'),
			('10+','10+'),

			)


		TIME_CATEGORY = (

			('', 'Time'),
			('10:00:00', '10 A.M'),
			('10:30:00 ', '10:30 A.M'),
			('11:00:00', '11 A.M'),
			('11:30:00', '11:30 A.M'),
			('12:00:00', '12 P.M'),
			('12:30:00', '12:30 P.M'),
			('13:00:00', '1 P.M'),
			('13:30:00', '1:30 P.M'),
			('14:00:00', '2 P.M'),
			('14:30:00', '2:30 P.M'),
			('15:00:00', '3 P.M'),
			('15:30:00', '3:30 P.M'),
			('16:00:00', '4 P.M'),
			('16:30:00', '4:30 P.M'),
			('17:00:00', '5 P.M'),
			('17:30:00', '5:30 P.M'),
			('18:00:00', '6 P.M'),
			('18:30:00', '6:30 P.M'),
			('19:00:00', '7 P.M'),
			('19:30:00', '7:30 P.M'),
			('20:00:00', '8 P.M'),
			('20:30:00', '8:30 P.M'),
			('21:00:00', '9 P.M'),
			('21:30:00', '9:30 P.M'),
			('22:00:00', '10 P.M'),


			)
		widgets = {'persons':forms.Select(choices=PERSON_CATEGORY, attrs={'class':'form-control', 'id':'name', 
		'placeholder':'Persons'}),

		'time':forms.Select(choices=TIME_CATEGORY, attrs={'class':'form-control', 'id':'name', 
		'placeholder':'Time'}),

		'phone':forms.TextInput(attrs={'class':'form-control', 'id':'name', 'placeholder':'Phone'}),

		'name':forms.TextInput(attrs={'class':'form-control', 'id':'name', 'placeholder':'Name'}),
		'email':forms.TextInput(attrs={'class':'form-control', 'id':'name', 'placeholder':'Email'}),
		'date':forms.SelectDateWidget(attrs={'class':'form-control', 'id':'name', 'placeholder':'Date'})

		}
