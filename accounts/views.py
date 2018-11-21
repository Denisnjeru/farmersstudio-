from django.shortcuts import render, redirect
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
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib import messages
from django.contrib.auth import update_session_auth_hash
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
    return render(request, 'registration/my_account.html', {'page_title': page_title})


@login_required
def logout_view(request):
    logout(request)
    return render(request, 'registration/logged_out.html')


@login_required
def change_password(request):
    if request.method == 'POST':
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)  # Important!
            messages.success(request, 'Your password was successfully updated!')
            return redirect('accounts:password_change_done')
        else:
            messages.error(request, 'Please correct the error below.')
    else:
        form = PasswordChangeForm(request.user)
    return render(request, 'registration/password_change_form.html', {'form': form})


@login_required
def password_change_done(request):
    return render(request, 'registration/password_change_done.html')
