from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def catalog(request):
    return HttpResponse("you are at the catalog index")
def home(request):
    return render(request, 'index.html')
