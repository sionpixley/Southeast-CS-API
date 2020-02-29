from django.http import HttpResponse
from django.http.response import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from rest_framework import status
from api.models import announcement, event, article, contact, admin
from api.serializers import announcement_serializer, event_serializer, article_serializer
from api.serializers import contact_serializer, admin_serializer


"""
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
"""

@csrf_exempt
def validate_admin(request):
    if request.method != "POST":
        return HttpResponse(status=status.HTTP_400_BAD_REQUEST)

    admin_dict = JSONParser().parse(request)

    try:
        check_admin = admin.objects.get(username=admin_dict["username"], passwd=admin_dict["passwd"])
        return HttpResponse(status=status.HTTP_200_OK)
    except admin.DoesNotExist:
        return HttpResponse(status=status.HTTP_404_NOT_FOUND)

@csrf_exempt
def get_all_admins(request):
    if request.method != "GET":
        return HttpResponse(status=status.HTTP_400_BAD_REQUEST)

    admins = admin.objects.all().distinct()
    admins_dict = admin_serializer(admins, many=True)
    return JsonResponse(admins_dict.data, safe=False)

@csrf_exempt
def add_announcement(request):
    if request.method != "POST":
        return HttpResponse(status=status.HTTP_400_BAD_REQUEST)

    announcement_dict = JSONParser().parse(request)

    try:
        check_announcement = announcement.objects.get(
            author=announcement_dict["author"],
            authored_date=announcement_dict["authored_date"],
            subject=announcement_dict["subject"],
            description=announcement_dict["description"]
        )
        return HttpResponse(status=status.HTTP_302_FOUND)
    except announcement.DoesNotExist:
        new_announcement = announcement_serializer(data=announcement_dict)
        if new_announcement.is_valid():
            new_announcement.save()
            return HttpResponse(status=status.HTTP_201_CREATED)
        else:
            return HttpResponse(status=status.HTTP_400_BAD_REQUEST)

@csrf_exempt
def get_announcement_by_id(request, id):
    if request.method != "GET":
        return HttpResponse(status=status.HTTP_400_BAD_REQUEST)

    try:
        check_announcement = announcement.objects.get(id=id)
        announcement_dict = announcement_serializer(check_announcement)
        return JsonResponse(announcement_dict.data)
    except announcement.DoesNotExist:
        return HttpResponse(status=status.HTTP_404_NOT_FOUND)

@csrf_exempt
def get_all_announcements(request):
    if request.method != "GET":
        return HttpResponse(status=status.HTTP_400_BAD_REQUEST)

    check_announcements = announcement.objects.all().distinct()
    announcements_dict = announcement_serializer(check_announcements, many=True)
    return JsonResponse(announcements_dict.data, safe=False)

@csrf_exempt
def edit_announcement_by_id(request, id, field):
    if (request.method != "PATCH") or (field == "id"):
        return HttpResponse(status=status.HTTP_400_BAD_REQUEST)

    announcement_dict = JSONParser().parse(request)

    try:
        check_announcement = announcement.objects.get(id=id)
        if field == "author":
            check_announcement.author = announcement_dict["author"]
            check_announcement.save()
        elif field == "authored_date":
            check_announcement.authored_date = announcement_dict["authored_date"]
            check_announcement.save()
        elif field == "subject":
            check_announcement.heading = announcement_dict["subject"]
            check_announcement.save()
        elif field == "description":
            check_announcement.info = announcement_dict["description"]
            check_announcement.save()
        else:
            return HttpResponse(status=status.HTTP_400_BAD_REQUEST)
        return HttpResponse(status=status.HTTP_200_OK)
    except announcement.DoesNotExist:
        return HttpResponse(status=status.HTTP_404_NOT_FOUND)

@csrf_exempt
def remove_announcement_by_id(request, id):
    if request.method != "DELETE":
        return HttpResponse(status=status.HTTP_400_BAD_REQUEST)

    try:
        check_announcement = announcement.objects.get(id=id)
        check_announcement.delete()
        return HttpResponse(status=status.HTTP_200_OK)
    except announcement.DoesNotExist:
        return HttpResponse(status=status.HTTP_404_NOT_FOUND)
