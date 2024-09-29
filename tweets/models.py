from django.db import models
from common.models import CommonModel

# Create your models here.
class Tweet(CommonModel):
    """ Model Definition for Tweets """
    payload = models.TextField(max_length=180)
    user = models.ForeignKey(
        "users.User",
        on_delete=models.CASCADE,
        related_name="tweets",
    )
    def __str__(self):
        return self.payload

class Like(CommonModel):
    """ Model Definition for Likes """
    user = models.ForeignKey(
        "users.User",
        on_delete=models.CASCADE,
        related_name="likes",
    )
    tweet = models.ForeignKey(
        "tweets.Tweet",
        on_delete=models.CASCADE,
        related_name="likes",
    )
    def __str__(self):
        return f"[{self.user.username}] {self.tweet.payload}"