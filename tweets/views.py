from django.shortcuts import render
from django.http import HttpResponse
from tweets.models import Tweet

# Create your views here.
def list(request):
    tweets = Tweet.objects.all()
    return render(
        request,
        "list.html",
        {
            "tweets": tweets,
            "title": "This is Tweets",
        }
    )

def detail(request, tweet_pk):
    try:
        tweet = Tweet.objects.get(pk=tweet_pk)
        return render(
            request,
            "detail.html",
            {
                "tweet": tweet,
            }
        )
    except Tweet.DoesNotExist:
        return render(
            request,
            "detail.html",
            {
                "not_found": True,
            }
        )

