from django.test import TestCase
from django.contrib.auth import authenticate, get_user_model

# Create your tests here.


class test_for_users(TestCase):


	def test_for_user_model(self):

		email='kotechashubham94@gmail.com'
		password='password123'
		user=get_user_model().objects.create_user(
			email=email,
			password=password
			)

		self.assertEqual(user.email, email)
		self.assertTrue(user.check_password(password))


	def test_for_normalizing_email(self):

		email='kotechashubham94@Gmail.com'
		password='password123'
		user=get_user_model().objects.create_user(
			email=email,
			password=password
			)

		self.assertEqual(user.email, email.lower())