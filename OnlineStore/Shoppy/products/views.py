from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.shortcuts import render, get_object_or_404
from .models import Product
from .forms import ProductForm
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

def new_product(request):
    if request.method == 'POST':
        form = ProductForm(request.POST)
        if form.is_valid():
            product = form.save()
            return HttpResponseRedirect('/')
    else:
        form = ProductForm()
    template = loader.get_template('new_product.html')
    context = {
        'form': form
    }
    return HttpResponse(template.render(context, request))