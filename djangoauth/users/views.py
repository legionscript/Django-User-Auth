from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django import views
from .forms import UserRegisterForm

class Index(views.View):
	def get(self, request):
		return render(request, 'users/index.html')

class Register(views.View):
	def get(self, request):
		form = UserRegisterForm()
		return render(request, 'users/register.html', {'form': form})

	def post(self, request):
		# render form with POST body data
		form = UserRegisterForm(request.POST)

		# check if form is vaild
		if form.is_valid():
			new_user = form.save()

			# if valid, save form and authenticate user
			new_user = authenticate(
				username=form.cleaned_data['username'],
				password=form.cleaned_data['password1'])

			login(request, new_user)

		# redirect when finished
		return redirect('index')
