from django.contrib import admin
from tweets.models import Tweet, Like


# Register your models here.
@admin.register(Tweet)
class TweetAdmin(admin.ModelAdmin):
    list_display = ('payload', 'user', 'created_at', 'updated_at')
    list_filter = ('user__username', 'created_at', 'updated_at')

@admin.register(Like)
class LikeAdmin(admin.ModelAdmin):
    list_display = ('tweet', 'user', 'created_at', 'updated_at')
    list_filter = ('user__username', 'created_at', 'updated_at')