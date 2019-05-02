from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.contrib.auth.models import User
import urllib, hashlib

def home(request):
	"""This function displays the home page"""
	if request.method != "GET":
		return HttpResponse("Method not allowed on /.", status=405)
	return HttpResponse(render(request, "main/index.html"), status=200)

def specificUser(request, user_id):
	"""This function displays the user page based on the given user id and creates
	a gravatar URL"""
	if request.method == 'GET':
		# Authenticates the user and redirects the user to the specified user id
		if request.user.is_authenticated:
			user = User.objects.get(id=user_id)
			
			# Get rid of trailing whitespace from email
			email = user.email.strip()

			# Create gravatar url by lowercasing and hashing the users email
			gravatar_url = "https://www.gravatar.com/avatar/" + hashlib.md5(email.lower().encode()).hexdigest() + "?"

			# Redirects user to user page
			return HttpResponse(render(request, "main/specificUser.html", {'user': user, 'gravatar': gravatar_url}),status=200)
		else:
			# Redirects the user to sign in they aren't already logged in
			return HttpResponseRedirect('/auth/signin')
    # Redirects to another page if given any other request
	return HttpResponse("Method not allowed on /main/users/.", status=405)