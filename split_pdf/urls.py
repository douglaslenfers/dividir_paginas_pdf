from django.conf.urls import url
from django.contrib import admin
from django.conf.urls import patterns, include, url
from views import index
urlpatterns = [
    url('', index)
]