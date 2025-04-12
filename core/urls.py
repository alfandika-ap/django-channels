from django.contrib import admin
from django.urls import path, include
from .consumer import NotificationConsumer

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include("notifications.urls")),
]

websocket_urlpatterns = [path("ws/notifications/", NotificationConsumer.as_asgi())]
