from django.shortcuts import render
from django.contrib.auth import authenticate, login
from django.http import HttpResponseRedirect, HttpResponse
from django.core.urlresolvers import reverse
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django import forms

# Create your views here.
def login_form(request):
  return render(request, 'submit/login.html', {})

def submitlogin(request):
  Username = request.POST['username']
  Password = request.POST['password']
  user = authenticate(username=Username, password=Password)
  if user is not None:
    if user.is_active:
      login(request, user)
      return HttpResponseRedirect('profile')
  return HttpResponseRedirect('login')

@login_required
def profile(request):
  context = {'username': request.user.username}
  return render(request, 'submit/profile.html', context)

class UserRegistrationForm(forms.Form):
  username = forms.CharField(label=u'username')
  password = forms.CharField(label=u'password')
  email = forms.CharField(label=u'email')
  first_name = forms.CharField(label=u'first_name')
  last_name = forms.CharField(label=u'last_name')

def register(request):
  if request.method == 'POST':
    form = UserRegistrationForm(request.POST)
    if form.is_valid():
      User.objects.create_user(form.cleaned_data['username'],
                               form.cleaned_data['email'],
                               form.cleaned_data['password'],
                  first_name=form.cleaned_data['first_name'],
                  last_name=form.cleaned_data['last_name'],)
      user = authenticate(username=form.cleaned_data['username'],
                          password=form.cleaned_data['password'])
      login(request, user)
      return HttpResponseRedirect('profile')
  form = UserRegistrationForm()
  return render(request, 'submit/register.html', {'form': form})
