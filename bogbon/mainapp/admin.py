# InternalImports
from .models import Article
# End InternalImports

# DjangoImports
from django.contrib import admin
# End DjangoImports

# ExternalImports
from django_summernote.admin import SummernoteModelAdmin
# End ExternalImports


class ArticleConfig(SummernoteModelAdmin):
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


admin.site.register(Article, ArticleConfig)
