from rest_framework import serializers
from api.models import announcement, event, article, contact, admin


class announcement_serializer(serializers.ModelSerializer):
    class Meta:
        model = announcement
        fields = ("id", "author", "authored_date", "subject", "description")


class event_serializer(serializers.ModelSerializer):
    class Meta:
        model = event
        fields = ("id", "date", "location", "name", "description", "organization")


class article_serializer(serializers.ModelSerializer):
    class Meta:
        model = article
        fields = ("id", "subject", "description")


class contact_serializer(serializers.ModelSerializer):
    class Meta:
        model = contact
        fields = ("id", "name", "email", "phone", "office")


class admin_serializer(serializers.ModelSerializer):
    class Meta:
        model = admin
        fields = ("id", "username", "passwd")
