from django.urls import path

from . import views

urlpatterns = [
    path('blog/post/<str:permalink>', views.blog_post, name='blog_name'),
    path(r'blog/search/', views.blog_search, name='blog_search'),
    path('blog/', views.blog, name='blog'),
    path('about/', views.about, name='about'),
    path('', views.index, name='index')
]