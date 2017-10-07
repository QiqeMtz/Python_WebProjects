from django.http import HttpResponse
from django.template import loader
from django.shortcuts import render, get_object_or_404
from .models import Product
# Create your views here.

def hello_word(request):
    #return HttpResponse('Hello World')
    #return render(request, 'index.html')+
    product = Product.objects.order_by('id')
    template = loader.get_template('index.html')
    title = 'Product List'
    context = {
        'product': product,
        'title': title
    }
    return HttpResponse(template.render(context, request))

def product_detail(request, pk):
    # Busca un objeto en la base de datos y su primary key, si no los encuentra devuelve un Error 404
    product = get_object_or_404(Product, pk=pk)
    template = loader.get_template('product_detail.html')
    title = 'Product Details'
    context = {
        'product': product,
        'title': title
    }
    return HttpResponse(template.render(context, request))