from django.http import HttpResponse
from django.http.response import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from rest_framework import status
from api.models import announcement, event, article, contact, admin
from api.serializers import announcement_serializer, event_serializer, article_serializer, contact_serializer, admin_serializer


@csrf_exempt
def add_admin(request):
    if request.method != "POST":
        return HttpResponse(status=status.HTTP_400_BAD_REQUEST)

    admin_dict = JSONParser().parse(request)

    try:
        check_admin = admin.objects.get(username=admin_dict["username"])
        return HttpResponse(status=status.HTTP_302_FOUND)
    except admin.DoesNotExist:
        new_admin = admin_serializer(data=admin_dict)
        if new_admin.is_valid():
            new_admin.save()
            return HttpResponse(status=status.HTTP_201_CREATED)
        else:
            return HttpResponse(status=status.HTTP_400_BAD_REQUEST)

@csrf_exempt
def get_all_admins(request):
    if request.method != "GET":
        return HttpResponse(status=status.HTTP_400_BAD_REQUEST)

    admins = admin.objects.all().distinct()
    admins_dict = admin_serializer(admins, many=True)
    return JsonResponse(admins_dict.data, safe=False)
