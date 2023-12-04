from django.urls import path
from . import views
from .views import chat_view

urlpatterns = [
    path("", views.base, name='base'),
    path("home/", views.home, name="home"),
    path("chatbox/", views.chatbox, name="chatbox"),
    path("inventory/", views.inventory, name="inventory"),
    path("about/", views.about, name="about"),
    path('chat/', chat_view, name='chat_view')
]