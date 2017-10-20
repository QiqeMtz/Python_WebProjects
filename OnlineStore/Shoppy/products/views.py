from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.shortcuts import render, get_object_or_404

from django.views.generic import ListView
from django.views.generic.detail import DetailView

from .models import Product
from .forms import ProductForm
# Create your views here.

def hello_word(request):
    #return HttpResponse('Hello World')
    #return render(request, 'index.html')+
    product = Product.objects.order_by('id')
    template = loader.get_template('index.html')
    title = 'Product List - Django'
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
        # request.FILES se usa cuando se trabaja con archivos en los formularios
        form = ProductForm(request.POST, request.FILES)
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

# using class based views
class ProductList(ListView):
    model = Product

class ProductDetail(DetailView):
    model = Product
