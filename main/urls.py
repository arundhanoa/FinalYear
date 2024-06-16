# main/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.homepage, name='homepage'),
    path('other/', views.other_page, name='other_page'),  # This is an example for linking to another page
]
