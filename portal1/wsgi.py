"""
WSGI config for nsa_collaboration project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/1.6/howto/deployment/wsgi/
"""

import os
# import sys
# path = '/Users/arashaga/Documents/Django_Projects/portal1'
# if path not in sys.path:
# sys.path.append(path)
#
# sys.path.insert(0,'/Users/arashaga/Documents/Django_Projects/portal1/')
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "portal1.settings")

from django.core.wsgi import get_wsgi_application

application = get_wsgi_application()
