from django.urls import path
from tweets import views

urlpatterns = [
    path("tweets/", views.listAll),
    path("tweets/<int:tweet_pk>", views.detail),
    path("users/<int:user_pk>/tweets", views.list),
]