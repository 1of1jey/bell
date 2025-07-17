from django import forms

class SignupForm(forms.Form):
    mobile = forms.CharField(max_length=15, label='Mobile Number')
    password = forms.CharField(widget=forms.PasswordInput, label='Password')

class LoginForm(forms.Form):
    mobile = forms.CharField(max_length=15, label='Mobile Number')
    password = forms.CharField(widget=forms.PasswordInput, label='Password') 