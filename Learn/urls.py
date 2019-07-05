from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^tags/$', views.learnTags, name='tag'),
    url(r'^tag-articles/$', views.tagArticles, name='tag'),
]