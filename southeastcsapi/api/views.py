from django.http import HttpResponse
from django.http.response import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from rest_framework import status
from api.models import announcement, event, article, contact
from api.serializers import announcement_serializer, event_serializer, article_serializer, contact_serializer


