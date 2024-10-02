from django.urls import path
from tweets import views

urlpatterns = [
    path("", views.list),
    path("<int:tweet_pk>", views.detail),
]