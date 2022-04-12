# DjangoImports
from django.core.wsgi import get_wsgi_application
# End DjangoImports

# ExternalImports
import os
# End ExternalImports


# Config
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'bogbon.settings')
application = get_wsgi_application()
# End Config
