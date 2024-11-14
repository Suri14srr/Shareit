from django.urls import path
from channels.routing import ProtocolTypeRouter, URLRouter
from channels.auth import AuthMiddlewareStack
from django.core.asgi import get_asgi_application  # Import the get_asgi_application function
from .consumers import SyncConsumer  # Ensure the import path is correct

# Define your WebSocket URL patterns
websocket_urlpatterns = [
    path('ws/sync/', SyncConsumer.as_asgi()),  # This path should match your WebSocket URL
]

# Create the application instance
application = ProtocolTypeRouter({
    # HTTP requests are handled by Django's ASGI application
    "http": get_asgi_application(),
    # WebSocket requests are routed to the WebSocket consumers
    "websocket": AuthMiddlewareStack(
        URLRouter(websocket_urlpatterns)
    ),
})
