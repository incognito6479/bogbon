# DjangoImports
from django.shortcuts import render
from .models import News
# End DjangoImports


# Config
def news_list(request):
    template = 'news/news_list.html'
    news = News.objects.all()
    context = {
        'news': news,
    }
    return render(request, template, context)
# End Config
