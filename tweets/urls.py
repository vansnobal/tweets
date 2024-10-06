from django.urls import path
from tweets import views

urlpatterns = [
    path("tweets/", views.Tweets.as_view()),
    path("tweets/<int:tweet_pk>", views.TweetDetail.as_view()),
    path("users/<int:user_pk>/tweets", views.UserTweets.as_view()),
]