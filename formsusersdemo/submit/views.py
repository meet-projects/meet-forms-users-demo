from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse
from django.core.urlresolvers import reverse

# Create your views here.
def login(request):
	return render(request, 'submit/login.html', {})

def submitlogin(request):
	UserName = request.POST['username']
	Password = request.POST['password']
	
	return HttpResponseRedirect('profile')

def profile(request):
	context = {'username': 'Kyle'}
	return render(request, 'submit/profile.html', context)