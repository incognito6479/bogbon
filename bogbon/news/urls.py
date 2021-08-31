# InternalImports
from . import views
# End InternalImports

# DjangoImports
from django.urls import path
# End DjangoImports


# Config
app_name = 'news'
urlpatterns = [
    path('', views.news_list, name='news_list'),
]
# End Config
