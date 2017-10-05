from django.http import HttpResponse
from django.template import loader
from django.shortcuts import render

from .models import Gato
# Create your views here.

def gato(request):
    gatos = Gato.objects.order_by('id')
    template = loader.get_template('gato.html')
    title = 'Los gatos son cool'
    context = {
        'gatos': gatos,
        'title': title
    }
    return HttpResponse(template.render(context, request))