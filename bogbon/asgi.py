# DjangoImports
from django.core.asgi import get_asgi_application
# End DjangoImports

# ExternalImports
import os
# End ExternalImports


# Config
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'bogbon.settings')
application = get_asgi_application()
# End Config
