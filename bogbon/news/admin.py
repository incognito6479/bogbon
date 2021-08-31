# InternalImports
from .models import News
# End InternalImports

# DjangoImports
from django.contrib import admin
# End DjangoImports


# Config
class NewsConfig(admin.ModelAdmin):
    fields = ('name', 'date',)


admin.site.register(News, NewsConfig)
# End Config
