# coding=utf-8
from django.conf.urls import url
from . import views


urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^upload/$', views.file_upload, name='upload_file'),
]
