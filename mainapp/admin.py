from .models import Article, Category, Product, ProductPhoto
from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin


class ArticleAdmin(SummernoteModelAdmin):
    fields = (
        'name',
        'author',
        'short_description',
        'text',
        'name_uz',
        'author_uz',
        'short_description_uz',
        'text_uz',
        'name_en',
        'author_en',
        'short_description_en',
        'text_en',
        'pub_date',
        'img_preview',
        'img_background',
        'img_post',
    )
    summernote_fields = ('text', 'text_en', 'text_uz',)


class ProductAdmin(SummernoteModelAdmin):
    fields = (
        'title_ru',
        'title_uz',
        'title_en',
        'category',
        'subtitle_ru',
        'subtitle_uz',
        'subtitle_en',
        'price',
        'show_price',
        'description_ru',
        'description_uz',
        'description_en',
        'img_preview',
        'img_hover',
    )
    summernote_fields = ('description_ru', 'description_uz', 'description_en',)


class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name_en',), }


admin.site.register(Article, ArticleAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Product, ProductAdmin)
admin.site.register(ProductPhoto)
