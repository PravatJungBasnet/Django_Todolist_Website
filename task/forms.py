from django import forms
from .models import task
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
class taskfrom(forms.ModelForm):
    class Meta:
        model=task
        fields=['title','description','complete','task_priority','due_date','status',]
#signup
class Signup(UserCreationForm):
    password1=forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control'}))
    password2=forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control'}))
    class Meta:
        model=User
        fields={'username','email'}
        widgets={'username':forms.TextInput(attrs={'class':'form-control'})}