from django.conf.urls import url, include
from . import views
from django.urls import path

urlpatterns = [
    path("", views.index, name='index'),
    path("contact/", views.contact, name='contact')
]