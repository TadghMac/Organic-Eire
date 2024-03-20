from . import views
from django.urls import path

urlpatterns = [
    path('', views.links_me, name='links'),
]