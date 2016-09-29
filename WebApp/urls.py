from django.conf.urls import url

from . import views 

urlpatterns = [
    url(r'^$', views.index, name='hola'),
    url(r'^index/$', views.index, name='indexxx'),
    url(r'^([0-9])/$', views.index, name='indexnum'),
    #url(r'^$', gol),
]