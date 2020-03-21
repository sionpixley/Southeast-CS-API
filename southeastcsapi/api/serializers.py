from rest_framework import serializers
from api.models import announcement, event, course, contact, admin


class announcement_serializer(serializers.ModelSerializer):
    class Meta:
        model = announcement
        fields = ("id", "author", "authored_date", "subject", "description")


class event_serializer(serializers.ModelSerializer):
    class Meta:
        model = event
        fields = ("id", "date", "location", "name", "description", "organization")


class course_serializer(serializers.ModelSerializer):
    class Meta:
        model = course
        fields = ("id", "name", "number", "credits", "prerequisites", "availability", "description")


class contact_serializer(serializers.ModelSerializer):
    class Meta:
        model = contact
        fields = ("id", "name", "email", "phone", "office")


class admin_serializer(serializers.ModelSerializer):
    class Meta:
        model = admin
        fields = ("id", "username", "passwd")
