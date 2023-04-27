

from django.urls import path, include
from .views import SocketView

# from accounts.views import UserView



urlpatterns = [
    path('stream/', SocketView.as_view(), name='stream'),
]

