from .models import Article, Category, Product, ProductPhoto
from django.shortcuts import render, get_object_or_404, redirect
from django.db.models import Count
from django.views.generic import TemplateView, View
from .bot import send_user_data_to_group
from django.db.models import Q


class ProductDetailView(TemplateView):
    def get_template_names(self):
        template = ''
        if '/uz/' in self.request.path:
            template = 'mainapp/product/product_detail_uz.html'
        elif '/en/' in self.request.path:
            template = 'mainapp/product/product_detail_en.html'
        else:
            template = 'mainapp/product/product_detail.html'
        return template

    def get_context_data(self, **kwargs):
        context = super(ProductDetailView, self).get_context_data(**kwargs)
        product = Product.objects.get(id=self.kwargs['pk'])
        product_photo = ProductPhoto.objects.filter(product_id=self.kwargs['pk'])
        similar_products = Product.objects.select_related('category') \
                               .filter(~Q(id=self.kwargs['pk']), category_id=product.category_id)[:4]
        context['product'] = product
        context['product_photo'] = product_photo
        context['similar_products'] = similar_products
        return context


class OrderSend(View):
    def post(self, request):
        product = Product.objects.get(id=request.POST.get('product_id'))
        send_user_data_to_group(request.POST, product.title_ru)
        if '/uz/' in request.path:
            return redirect('mainapp:product_detail_uz', pk=request.POST.get('product_id'))
        elif '/en/' in request.path:
            return redirect('mainapp:product_detail_en', pk=request.POST.get('product_id'))
        return redirect('mainapp:product_detail', pk=request.POST.get('product_id'))


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


def product_list(request):
    categories = Category.objects.prefetch_related('product').annotate(product_count=Count('product')).all()
    products = Product.objects.all()
    if request.GET.get('category_id'):
        products = products.filter(category_id=request.GET.get('category_id'))
    context = {
        'categories': categories,
        'products': products,
        'category_id': request.GET.get('category_id')
    }
    if '/uz/' in request.path:
        template = 'mainapp/product/product_list_uz.html'
    elif '/en/' in request.path:
        template = 'mainapp/product/product_list_en.html'
    else:
        template = 'mainapp/product/product_list.html'
    return render(request, template, context)


def category_detail(request, category_slug):
    category = get_object_or_404(Category, slug=category_slug)
    context = {
        'category': category,
    }
    if '/uz/' in request.path:
        template = 'mainapp/product/category_detail_uz.html'
    elif '/en/' in request.path:
        template = 'mainapp/product/category_detail_en.html'
    else:
        template = 'mainapp/product/category_detail.html'
    return render(request, template, context)


def about(request):
    if '/uz/' in request.path:
        template = 'mainapp/about_uz.html'
    elif '/en/' in request.path:
        template = 'mainapp/about_en.html'
    else:
        template = 'mainapp/about.html'
    return render(request, template)


def seedling_list(request):
    if '/uz/' in request.path:
        template = 'mainapp/seedling/seedling_list_uz.html'
    elif '/en/' in request.path:
        template = 'mainapp/seedling/seedling_list_en.html'
    else:
        template = 'mainapp/seedling/seedling_list.html'
    return render(request, template)
