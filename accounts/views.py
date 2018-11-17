from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm
from django.template import RequestContext
from django.shortcuts import render_to_response, get_object_or_404
# from django.core import urlresolvers
from django.http import HttpResponseRedirect
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth.decorators import login_required
# Create your views here.


def register(request):
    if request.method == 'POST':
        postdata = request.POST.copy()
        form = UserCreationForm(postdata)
        if form.is_valid():
            form.save()
            un = postdata.get('username', '')
            pw = postdata.get('password1', '')
            from django.contrib.auth import login, authenticate
            new_user = authenticate(username=un, password=pw)
            if new_user and new_user.is_active:
                login(request, new_user)
                return HttpResponseRedirect(reverse('my_account'))
    else:
        form = UserCreationForm()
    page_title = 'User Registration'
    return render(request, 'registration/register.html', {'page_title': page_title, 'form': form})

@login_required
def my_account(request):
    page_title = "My Account"
    return render(request, 'registration/my_account', {'page_title':page_title})
