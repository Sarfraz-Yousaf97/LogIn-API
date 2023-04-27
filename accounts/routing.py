from django.urls import re_path

from .consumer import CameraStreamConsumer

websocket_urlpatterns = [
    re_path(r'^ws/camera-stream/$', CameraStreamConsumer.as_asgi()),
]