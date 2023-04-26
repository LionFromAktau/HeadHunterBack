"""
ASGI config for src project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/4.2/howto/deployment/asgi/
"""

import os

from channels.routing import ProtocolTypeRouter, URLRouter
from channels.security.websocket import AllowedHostsOriginValidator
from channels.sessions import SessionMiddlewareStack
from django.core.asgi import get_asgi_application
from api import routing

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'src.settings')

application = ProtocolTypeRouter({
        "http": get_asgi_application(),
        "websocket": AllowedHostsOriginValidator(
            SessionMiddlewareStack(
                URLRouter(
                    routing.websocket_urlpatterns
                )
            )
        ),
    })
