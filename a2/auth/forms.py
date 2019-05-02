from django import forms

# This creates the registration form
class RegistrationForm(forms.Form):
    username = forms.CharField(label='Username', max_length=30, required=True)
    password = forms.CharField(label='Password', max_length=30, required=True, widget=forms.PasswordInput)
    passwordconf = forms.CharField(label='Confirm Password', max_length=30, required=True, widget=forms.PasswordInput)
    email = forms.CharField(label='Email', max_length=30, required=True)
    first_name = forms.CharField(label='First Name', max_length=30, required=True)
    last_name = forms.CharField(label='Last Name', max_length=30, required=True)

# This creates the signin form
class SignInForm(forms.Form):
    username = forms.CharField(label='Username', max_length=30, required=True)
    password = forms.CharField(label='Password', max_length=30, required=True, widget=forms.PasswordInput)
