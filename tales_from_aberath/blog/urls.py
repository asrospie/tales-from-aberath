from django.urls import path

from . import views

urlpatterns = [
    path('blog', views.blog, name='blog'),
    path('about', views.about, name='about'),
    path('', views.index, name='index')
]