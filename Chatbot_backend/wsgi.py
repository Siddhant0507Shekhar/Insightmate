"""
WSGI config for Chatbot_backend project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/4.2/howto/deployment/wsgi/
"""
#
# import os
#
# from django.core.wsgi import get_wsgi_application
#
# os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'Chatbot_backend.settings')
#
# application = get_wsgi_application()

import os
import sys

path = '/path/to/your/django/project'
if path not in sys.path:
    sys.path.append(path)

os.environ['DJANGO_SETTINGS_MODULE'] = 'your_project.settings'

from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()

