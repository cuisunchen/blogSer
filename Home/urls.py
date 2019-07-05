from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^nav/$', views.nav, name='nav'),
    url(r'^aticles/$', views.aticles, name='aticles'),
    url(r'^search/$', views.search, name='search'),
]