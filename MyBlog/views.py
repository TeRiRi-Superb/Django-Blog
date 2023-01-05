from django.shortcuts import render, redirect, HttpResponseRedirect
from django.views.generic import View
from django.utils.timezone import utc
from django.core.paginator import Paginator
from django.contrib import messages
from .models import *

import markdown


# 主页
class Index(View):
    def get(self, request):
        page = request.GET.get('page',1)
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

        Article_Pages = paginator.page(page)

        for a in Article_Pages:
            tags = Tag.objects.filter(article=a)
            comment_count = Comment.objects.filter(article=a).count()
            a.taglist = tags
            a.comment_count = comment_count

        context = {
            'Article': Article_Pages,
            'pages': pages,
            'New_Article': New_Article,
            'Category': Cate,
        }

        return render(request,'index1.html',context)

# 帖子页
class Single(View):
    def get(self, request, id):
        Blog = Article.objects.get(id=id)
        comment = Comment.objects.filter(article_id=id).order_by('-create')

        Blog.content = markdown.markdown(Blog.content,
                                     extensions=[
                                      'markdown.extensions.extra',
                                      'markdown.extensions.codehilite',
                                      'markdown.extensions.toc',
                                  ],
                                  safe_mode=True,
                                  enable_attributes=False)

        tagname = Tag.objects.get(article=Blog).tname
        Blog.tname = tagname

        context = {
            'Blog': Blog,
            'Comment': comment,
        }
        return render(request,'article.html',context)

    def post(self, request, id):
        name = request.POST.get('name')
        email = request.POST.get('email')
        url = request.POST.get('url')
        comment = request.POST.get('comment')

        if name == '' or comment == '':
            messages.error(request, '名字或评论为空')
            return HttpResponseRedirect(request.path)

        Comment.objects.create(name=name, email=email, url=url, content=comment, article_id=id)
        return HttpResponseRedirect(request.path)

# 分类
class CateView(View):
    def get(self, request):
        page = request.GET.get('page', 1)
        Article_List = Article.objects.all()
        Cate = Category.objects.all()

        for c in Cate:
            Cate_count = Article.objects.filter(category__cname=c.cname).count()
            c.counts = Cate_count

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

        Article_Pages = paginator.page(page)

        for a in Article_Pages:
            tags = Tag.objects.filter(article=a)
            comment_count = Comment.objects.filter(article=a).count()
            a.taglist = tags
            a.comment_count = comment_count

        context = {
            'Article': Article_Pages,
            'pages': pages,
            'Category': Cate,
        }

        return render(request, 'category.html', context)

# 标签页
class TagView(View):
    def get(self, request):
        page = request.GET.get('page', 1)
        Article_List = Article.objects.all()
        Tag_List = Tag.objects.all()

        for t in Tag_List:
            Tag_count = Article.objects.filter(tag=t).count()
            print(type(t))
            t.counts = Tag_count

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

        Article_Pages = paginator.page(page)

        for a in Article_Pages:
            tags = Tag.objects.filter(article=a)
            comment_count = Comment.objects.filter(article=a).count()
            a.taglist = tags
            a.comment_count = comment_count

        context = {
            'Article': Article_Pages,
            'pages': pages,
            'Tag': Tag_List,
        }

        return render(request, 'tag.html', context)

# 归档
class ArchiveView(View):
    def get(self, request):
        article = Article.objects.all()

        context = {
            'article': article,
        }

        return render(request, 'archive.html', context)


class LinkView(View):
    def get(self, request):
        return render(request,'link.html')

