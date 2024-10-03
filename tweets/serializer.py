from rest_framework import serializers

class TweetSerializer(serializers.Serializer):
    pk = serializers.IntegerField()
    payload = serializers.CharField(
        required=True,
        max_length=180
    )
    created_at = serializers.DateTimeField()
    updated_at = serializers.DateTimeField()