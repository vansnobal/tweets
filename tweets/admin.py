from django.contrib import admin
from tweets.models import Tweet, Like

class ElonMuskFilter(admin.SimpleListFilter):
    title = "Filter by keyword - Elon Musk"
    parameter_name = 'keyword'
    def lookups(self, request, model_admin):
        return [("Elon Musk", "Elon Musk"),]
    def queryset(self, request, tweets):
        word = self.value()
        if word:
            return tweets.filter(payload__contains=word)
        else:
            return tweets

# Register your models here.
@admin.register(Tweet)
class TweetAdmin(admin.ModelAdmin):
    list_display = ('payload', 'user', 'created_at', 'updated_at')
    list_filter = ('created_at', ElonMuskFilter)
    search_fields = ('payload', 'user__username',)

@admin.register(Like)
class LikeAdmin(admin.ModelAdmin):
    list_display = ('tweet', 'user', 'created_at', 'updated_at')
    list_filter = ('created_at',)
    search_fields = ('user__username',)