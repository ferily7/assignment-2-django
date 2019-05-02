from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.views.decorators.debug import sensitive_post_parameters
from .forms import RegistrationForm
from .forms import SignInForm

@sensitive_post_parameters()
def register(request):
    """This function displays the registration form to the user and registers
    the user with the given information"""
    if request.method == 'GET':
        # Displays the registration form to the user
        form = RegistrationForm()
        return HttpResponse(render(request, "auth/register.html", {'form': form}),status=200)
    elif request.method == 'POST':
        form = RegistrationForm(request.POST)

        # This validates the information the user provides in the form
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            passwordconf = form.cleaned_data['passwordconf']
            email = form.cleaned_data['email']
            first_name = form.cleaned_data['first_name']
            last_name = form.cleaned_data['last_name']

            # Checks to see if the passwords are the same
            if password != passwordconf:
                return HttpResponse("Passwords did not match.", status=400)

            # Creates a new user in the database and redirects the user to sign in
            user = User.objects.create_user(username,email,password)
            user.first_name = first_name
            user.last_name = last_name
            user.save()
            return HttpResponseRedirect('/auth/signin')
    # Redirects to another page if given any other request
    else:
        return HttpResponse("Method not allowed on /auth/register",status=405)

@sensitive_post_parameters()
def signin(request):
    """This function displays the sign in form to the user and asks the user to
    sign in with a username and password"""
    if request.method == 'GET':
        # Displays the sign in form for the user to sign in
        form = SignInForm()
        return HttpResponse(render(request, "auth/signin.html", {'form': form}),status=200)
    elif request.method == 'POST':
        form = SignInForm(request.POST)

        # Validates the username and password from the user
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']

            # Authenticates the user with the given username and password
            user = authenticate(request, username=username, password=password)

            # This logs the user in if the user exists
            if user is not None:
                login(request, user)
                return HttpResponseRedirect('/')
            # Redirects to error page if the user doesn't exist
            else:
                return HttpResponse("Invalid credentials.",status=401)
        else:
            return HttpResponse("Bad login form.",status=400)

def signout(request):
    """This function signs the user out if they choose to sign out"""
    if request.method == 'GET':
        # Authenticates that the user is logged in
        if request.user.is_authenticated:
            # Successfully logs the user out and redirects to sign out page
            logout(request)
            return HttpResponse("Sign out successful.",status=200)
        # This redirects the user to an error page if they are not logged in
        else:
            return HttpResponse("Not logged in.", status=200)
    # Redirects to another page if given any other request
    else:
        return HttpResponse("Method not allowed on auth/signout.",status=405)