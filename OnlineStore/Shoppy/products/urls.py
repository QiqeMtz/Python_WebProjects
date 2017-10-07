from django.conf.urls import url
from . import views
urlpatterns = [
    url(r'^$', views.hello_word, name='hello'),
    # Forma de decir - a partir de mi url root, /producto/ una primary key que contiene sólo números del 0 al 9
    url(r'^product/(?P<pk>[0-9]+)/$', views.product_detail, name='product_detail'),
]
