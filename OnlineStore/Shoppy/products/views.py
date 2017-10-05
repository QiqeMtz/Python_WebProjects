from django.http import HttpResponse
from django.template import loader
from django.shortcuts import render

# Create your views here.

def hello_word(request):
    #return HttpResponse('Hello World')
    #return render(request, 'index.html')