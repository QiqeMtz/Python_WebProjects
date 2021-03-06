from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.shortcuts import render, get_object_or_404, redirect

from django.views.generic import ListView
from django.views.generic.detail import DetailView

from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User

from django.contrib.auth.decorators import login_required

from .models import Product
from .forms import ProductForm

from .mixins import LoginRequiredMixin
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

#decorator to require login when the user try to add a new product
@login_required()
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

def auth_login(request):
    if request.method == 'POST':
        action = request.POST.get('action', None)
        username = request.POST.get('username', None)
        password = request.POST.get('password', None)

        if action== 'signup':
            user = User.objects.create_user(username=username, 
                                            password=password)
            user.save()
        elif action == 'login':
            user = authenticate(username=username, password=password)
            login(request, user)
            return redirect('/')
    context = {}
    return render(request, 'login/login.html', context)

# using class based views
class ProductList(ListView):
    model = Product


class ProductDetail(LoginRequiredMixin, DetailView):
    model = Product
