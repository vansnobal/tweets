from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.exceptions import NotFound
from tweets.models import Tweet
from tweets.serializer import TweetSerializer
from users.models import User

# Create your views here.
@api_view(['GET'])
def listAll(request):
    tweets = Tweet.objects.all()
    serializer = TweetSerializer(tweets, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def list(request, user_pk):
    try:
        user = User.objects.get(pk=user_pk)
        tweets = Tweet.objects.filter(user=user)
        serializer = TweetSerializer(tweets, many=True)
        return Response(serializer.data)
    except User.DoesNotExist:
        raise NotFound('User does not exist')

@api_view(['GET'])
def detail(request, tweet_pk):
    try:
        tweet = Tweet.objects.get(pk=tweet_pk)
        serializer = TweetSerializer(tweet)
        return Response(serializer.data)
    except Tweet.DoesNotExist:
        raise NotFound('Tweet does not exist')