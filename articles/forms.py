from django.forms import ModelForm
from django import forms
from .models import Users, Article

class ArticleForm(ModelForm):
	class Meta:
		model = Article
		fields = '__all__'
		exclude = ['numVisits', ]

class RegisterUserForm(ModelForm):
	password = forms.CharField(widget=forms.PasswordInput())
	class Meta:
		model = Users
		fields = '__all__'
		exclude = ['role', 'id']

class LoginForm(forms.Form):
    username = forms.CharField()
    email = forms.EmailField()
    password = forms.CharField(widget= forms.PasswordInput)
    remember_me = forms.BooleanField()

# class LoginForm(ModelForm):
# 	class Meta:
# 		model = LoginForm
# 		fields = '__all__'