from django.shortcuts import render
from django.http import JsonResponse
from django.views.generic import View
from django.core.paginator import Paginator
from .models import *


# Create your views here.
class Index(View):
    def get(self, request, page):
        Article_List = Article.objects.all()
        New_Article = Article.objects.filter().order_by('-create')[0:3]
        Cate = Category.objects.all()
        Tags = Tag.objects.all()

        for c in Cate:
            Cate_count = Article.objects.filter(category__cname=c.cname).count()
            c.counts = Cate_count

        try:
            page = int(page)
        except:
            page = 1

        paginator = Paginator(Article_List, 5)

        num_pages = paginator.num_pages

        if num_pages < 5:
            pages = range(1, num_pages + 1)
        elif page <= 3:
            pages = range(1, 6)
        elif num_pages - page < 2:
            pages = range(num_pages - 4, num_pages + 1)
        else:
            pages = range(page - 2, page + 3)

        order_pages = paginator.page(page)

        context = {
            'Article': order_pages,
            'pages': pages,
            'New_Article': New_Article,
            'Category': Cate,
            'Tags': Tags,
        }

        return render(request,'index.html',context)


class Single(View):
    def get(self, request, id):
        Blog = Article.objects.get(id=id)
        New_Article = Article.objects.filter().order_by('-create')[0:3]
        Cate = Category.objects.all()
        Tags = Tag.objects.all()

        for c in Cate:
            Cate_count = Article.objects.filter(category__cname=c.cname).count()
            c.counts = Cate_count

        context = {
            'Blog': Blog,
            'New_Article': New_Article,
            'Category': Cate,
            'Tags': Tags,
        }
        return render(request,'single.html',context)


class About(View):
    def get(self, request):
        return render(request, 'about.html')


class Contact(View):
    def get(self, request):
        return render(request, 'contact.html')


class Blogs(View):
    def get(self, request, page):
        Article_List = Article.objects.all()

        try:
            page = int(page)
        except:
            page = 1

        paginator = Paginator(Article_List, 5)

        num_pages = paginator.num_pages

        if num_pages < 5:
            pages = range(1, num_pages + 1)
        elif page <= 3:
            pages = range(1, 6)
        elif num_pages - page < 2:
            pages = range(num_pages - 4, num_pages + 1)
        else:
            pages = range(page - 2, page + 3)

        order_pages = paginator.page(page)

        context = {
            'Article': order_pages,
            'pages': pages,
            'order': 'order'
        }

        return render(request, 'full-width.html', context)


class CateLink(View):
    def get(self, request):
        pass
