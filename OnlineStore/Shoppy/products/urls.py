from django.conf.urls import url
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    url(r'^login/$', views.auth_login, name='authentication'),
    url(r'^logout$', auth_views.logout, {'next_page': '/'} , name='logout'),
    url(r'^$', views.ProductList.as_view() , name='hello'),
    # Forma de decir - a partir de mi url root, /producto/ una primary key que contiene sólo números del 0 al 9
    url(r'^product/(?P<pk>[0-9]+)/$', views.ProductDetail.as_view(), name='detail'),
    url(r'^product/new', views.new_product, name='new'),
]
