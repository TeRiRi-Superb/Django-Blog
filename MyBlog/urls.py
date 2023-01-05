"""untitled URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path, include, re_path
from MyBlog.views import *

urlpatterns = [
    # path('',Index.as_view(), name='index'),
    # path('blogs/',Blogs.as_view(), name='blogs'),
    path('category/', CateView.as_view(), name='category'),
    path('tag/', TagView.as_view(), name='tag'),
    path('archive/', ArchiveView.as_view(), name='archive'),
    path('link/', LinkView.as_view(), name='link'),

    # re_path(r'^catelink/(?P<page>.*)$', CateLink.as_view(), name='catelink'),
    # re_path(r'^taglink/(?P<page>.*)$', TagLink.as_view(), name='taglink'),
    re_path(r'^single/(?P<id>.*)$', Single.as_view(), name='single'),

    path('', Index.as_view(), name='index'),
]