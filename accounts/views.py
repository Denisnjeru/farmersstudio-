from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm
from django.template import RequestContext
from django.shortcuts import render_to_response, get_object_or_404
# from django.core import urlresolvers
from django.http import HttpResponseRedirect
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.contrib.auth import (authenticate, get_user_model, login, logout)
from .forms import UserLoginForm
# Create your views here.


def register(request):
    if request.method == 'POST':
        postdata = request.POST.copy()
        form = UserCreationForm(postdata)
        if form.is_valid():
            form.save()
            un = postdata.get('username', '')
            pw = postdata.get('password1', '')
            new_user = authenticate(username=un, password=pw)
            if new_user and new_user.is_active:
                login(request, new_user)
                return HttpResponseRedirect(reverse("accounts:my_account"))
    else:
        form = UserCreationForm()
    page_title = 'User Registration'
    return render(request, 'registration/register.html', {'page_title': page_title, 'form': form})


def login_view(request):
    page_title = 'User Login'
    next = request.GET.get('next')
    form = UserLoginForm(request.POST or None)
    if form.is_valid():
        username = form.cleaned_data.get('username')
        password = form.cleaned_data.get('password')
        user = authenticate(username=username, password=password)
        login(request, user)
        if next:
            HttpResponseRedirect(next)
        return HttpResponseRedirect(reverse("accounts:my_account"))
    return render(request, 'registration/login.html', {'form': form, 'page_title': page_title})



@login_required
def my_account(request):
    page_title = "My Account"
    return render(request, 'registration/my_account.html', {'page_title':page_title})

@login_required
def logout_view(request):
    logout(request)
    return render(request, 'registration/logged_out.html')

