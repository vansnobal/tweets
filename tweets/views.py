from rest_framework.response import Response
from rest_framework.exceptions import NotFound
from rest_framework.views import APIView

from tweets.models import Tweet
from tweets.serializer import TweetSerializer
from users.models import User

# Create your views here.
class Tweets(APIView):
    def get(self, request):
        tweets = Tweet.objects.all()
        serializer = TweetSerializer(tweets, many=True)
        return Response(serializer.data)

class TweetDetail(APIView):
    def get(self, request, tweet_pk):
        try:
            tweet = Tweet.objects.get(pk=tweet_pk)
            serializer = TweetSerializer(tweet)
            return Response(serializer.data)
        except Tweet.DoesNotExist:
            raise NotFound('Tweet does not exist')

class UserTweets(APIView):
    def get(self, request, user_pk):
        try:
            user = User.objects.get(pk=user_pk)

            tweets = Tweet.objects.filter(user=user)
            serializer = TweetSerializer(tweets, many=True)
            return Response(serializer.data)
        except User.DoesNotExist:
            raise NotFound('User does not exist')