from rest_framework import serializers
from api.models import announcement, event, article, contact

class announcement_serializer(serializers.ModelSerializer):
    class Meta:
        model = announcement
        fields = ("id", "author", "authored_date", "heading", "info")

class event_serializer(serializers.ModelSerializer):
    class Meta:
        model = event
        fields = ("id", "date", "location", "name", "info", "organization")

class article_serializer(serializers.ModelSerializer):
    class Meta:
        model = article
        fields = ("id", "heading", "info")

class contact_serializer(serializers.ModelSerializer):
    class Meta:
        model = contact
        fields = ("id", "name", "email", "phone", "office")
