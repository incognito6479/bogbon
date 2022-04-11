# DjangoImports
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path, include
# End DjangoImports


# Config
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('mainapp.urls', namespace='mainapp')),
    path('summernote/', include('django_summernote.urls')),
]
# End Config

# DebugConfig
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
# End DebugConfig
