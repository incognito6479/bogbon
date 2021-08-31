# InternalImports
from .models import Article
# End InternalImports

# DjangoImports
from django.shortcuts import render, get_object_or_404
# End DjangoImports


# Config
def index(request):
    if '/uz/' in request.path:
        template = 'mainapp/index_uz.html'
    elif '/en/' in request.path:
        template = 'mainapp/index_en.html'
    else:
        template = 'mainapp/index.html'
    return render(request, template)


def news_list(request):
    if '/uz/' in request.path:
        template = 'mainapp/news_list_uz.html'
    elif '/en/' in request.path:
        template = 'mainapp/news_list_en.html'
    else:
        template = 'mainapp/news_list.html'
    return render(request, template)


def article_list(request):
    articles = Article.objects.all().order_by('-pub_date')
    context = {
        'articles': articles,
    }
    if '/uz/' in request.path:
        template = 'mainapp/article/article_list_uz.html'
    elif '/en/' in request.path:
        template = 'mainapp/article/article_list_en.html'
    else:
        template = 'mainapp/article/article_list.html'
    return render(request, template, context)


def article_detail(request, id):
    article = get_object_or_404(Article, id=id)
    context = {
        'article': article,
    }
    if '/uz/' in request.path:
        template = 'mainapp/article/article_detail_uz.html'
    elif '/en/' in request.path:
        template = 'mainapp/article/article_detail_en.html'
    else:
        template = 'mainapp/article/article_detail.html'
    return render(request, template, context)
# End Config
