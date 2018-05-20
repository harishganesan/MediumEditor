

# Create your views here.
from django.http import HttpResponseRedirect
from django.shortcuts import render



def get_name(request):


    return render(request, 'index.html', {})