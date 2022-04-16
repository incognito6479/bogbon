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
        'subtitle_ru',
        'description_ru',
        'title_uz',
        'subtitle_uz',
        'description_uz',
        'title_en',
        'subtitle_en',
        'description_en',
        'price',
        'show_price',
        'category',
        'img_preview',
        'img_hover',
    )
    summernote_fields = ('description_ru', 'description_uz', 'description_en',)


class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name_en',), }


admin.site.register(Article, ArticleAdmin)
admin.site.register(Category, CategoryAdmin)
# admin.site.register(ProductPhoto)
# admin.site.register(Product, ProductAdmin)


class ProductPhotoInline(admin.TabularInline):
    model = ProductPhoto
    min_num = 2
    extra = 0


@admin.register(Product)
class ProductModelAdmin(ProductAdmin, admin.ModelAdmin):
    inlines = [
        ProductPhotoInline
    ]
