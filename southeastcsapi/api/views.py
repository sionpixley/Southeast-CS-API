from django.http import HttpResponse
from django.http.response import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from rest_framework import status
from api.models import announcement, event, article, contact, admin
from api.serializers import announcement_serializer, event_serializer, article_serializer
from api.serializers import contact_serializer, admin_serializer


@csrf_exempt
def add_admin(request):
    if request.method != "POST":
        return HttpResponse(status=status.HTTP_400_BAD_REQUEST, reason="Must use POST method.")

    admin_dict = JSONParser().parse(request)

    try:
        check_admin = admin.objects.get(username=admin_dict["username"])
        return HttpResponse(status=status.HTTP_302_FOUND, reason="Admin account already exists")
    except admin.DoesNotExist:
        new_admin = admin_serializer(data=admin_dict)
        if new_admin.is_valid():
            new_admin.save()
            return HttpResponse(status=status.HTTP_201_CREATED, reason="New admin created.")
        else:
            return HttpResponse(status=status.HTTP_400_BAD_REQUEST, reason="Object was not in a valid form.")

@csrf_exempt
def validate_admin(request):
    if request.method != "POST":
        return HttpResponse(status=status.HTTP_400_BAD_REQUEST, reason="Must use POST method.")

    admin_dict = JSONParser().parse(request)

    try:
        check_admin = admin.objects.get(username=admin_dict["username"], passwd=admin_dict["passwd"])
        return HttpResponse(status=status.HTTP_200_OK, reason="Admin exists and their password is correct.")
    except admin.DoesNotExist:
        return HttpResponse(status=status.HTTP_404_NOT_FOUND, reason="Admin doesn't exist or password is incorrect.")

@csrf_exempt
def get_all_admins(request):
    if request.method != "GET":
        return HttpResponse(status=status.HTTP_400_BAD_REQUEST, reason="Must use GET method.")

    check_admins = admin.objects.all().distinct()
    admins_dict = admin_serializer(check_admins, many=True)
    return JsonResponse(admins_dict.data, safe=False)

@csrf_exempt
def add_announcement(request):
    if request.method != "POST":
        return HttpResponse(status=status.HTTP_400_BAD_REQUEST, reason="Must use POST method.")

    announcement_dict = JSONParser().parse(request)

    try:
        check_announcement = announcement.objects.get(
            author=announcement_dict["author"],
            authored_date=announcement_dict["authored_date"],
            subject=announcement_dict["subject"]
        )
        return HttpResponse(status=status.HTTP_302_FOUND, reason="Announcement already exists.")
    except announcement.DoesNotExist:
        new_announcement = announcement_serializer(data=announcement_dict)
        if new_announcement.is_valid():
            new_announcement.save()
            return HttpResponse(status=status.HTTP_201_CREATED, reason="New announcement created.")
        else:
            return HttpResponse(status=status.HTTP_400_BAD_REQUEST, reason="Object was not in a valid form.")

@csrf_exempt
def get_announcement_by_id(request, id):
    if request.method != "GET":
        return HttpResponse(status=status.HTTP_400_BAD_REQUEST, reason="Must use GET method.")

    try:
        check_announcement = announcement.objects.get(id=id)
        announcement_dict = announcement_serializer(check_announcement)
        return JsonResponse(announcement_dict.data)
    except announcement.DoesNotExist:
        return HttpResponse(status=status.HTTP_404_NOT_FOUND, reason="Announcement does not exist.")

@csrf_exempt
def get_all_announcements(request):
    if request.method != "GET":
        return HttpResponse(status=status.HTTP_400_BAD_REQUEST, reason="Must use GET method.")

    check_announcements = announcement.objects.all().distinct()
    announcements_dict = announcement_serializer(check_announcements, many=True)
    return JsonResponse(announcements_dict.data, safe=False)

@csrf_exempt
def edit_announcement_by_id(request, id, field):
    if request.method != "PATCH":
        return HttpResponse(status=status.HTTP_400_BAD_REQUEST, reason="Must use PATCH method.")
    elif field == "id":
        return HttpResponse(status=status.HTTP_400_BAD_REQUEST, reason="Cannot edit the id field.")

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
            return HttpResponse(status=status.HTTP_400_BAD_REQUEST, reason="Must enter a valid field.")
        return HttpResponse(status=status.HTTP_200_OK, reason="Announcement updated.")
    except announcement.DoesNotExist:
        return HttpResponse(status=status.HTTP_404_NOT_FOUND, reason="Announcement does not exist.")

@csrf_exempt
def remove_announcement_by_id(request, id):
    if request.method != "DELETE":
        return HttpResponse(status=status.HTTP_400_BAD_REQUEST, reason="Must use DELETE method.")

    try:
        check_announcement = announcement.objects.get(id=id)
        check_announcement.delete()
        return HttpResponse(status=status.HTTP_200_OK, reason="Announcement removed from database.")
    except announcement.DoesNotExist:
        return HttpResponse(status=status.HTTP_404_NOT_FOUND, reason="Announcement does not exist.")

@csrf_exempt
def add_event(request):
    if request.method != "POST":
        return HttpResponse(status=status.HTTP_400_BAD_REQUEST, reason="Must use POST method.")

    event_dict = JSONParser().parse(request)

    try:
        check_event = event.objects.get(
            date=event_dict["date"],
            location=event_dict["location"],
            name=event_dict["name"]
        )
        return HttpResponse(status=status.HTTP_302_FOUND, reason="Event already exists.")
    except event.DoesNotExist:
        new_event = event_serializer(data=event_dict)
        if new_event.is_valid():
            new_event.save()
            return HttpResponse(status=status.HTTP_201_CREATED, reason="New event created.")
        else:
            return HttpResponse(status=status.HTTP_400_BAD_REQUEST, reason="Object was not in valid form.")

@csrf_exempt
def get_event_by_id(request, id):
    if request.method != "GET":
        return HttpResponse(status=status.HTTP_400_BAD_REQUEST, reason="Must use GET method.")

    try:
        check_event = event.objects.get(id=id)
        event_dict = event_serializer(check_event)
        return JsonResponse(event_dict.data)
    except event.DoesNotExist:
        return HttpResponse(status=status.HTTP_404_NOT_FOUND, reason="Event does not exist.")

@csrf_exempt
def get_all_events(request):
    if request.method != "GET":
        return HttpResponse(status=status.HTTP_400_BAD_REQUEST, reason="Must use GET method.")

    check_events = event.objects.all().distinct()
    events_dict = event_serializer(check_events, many=True)
    return JsonResponse(events_dict.data, safe=False)

@csrf_exempt
def edit_event_by_id(request, id, field):
    if request.method != "PATCH":
        return HttpResponse(status=status.HTTP_400_BAD_REQUEST, reason="Must use PATCH method.")
    elif field == "id":
        return HttpResponse(status=status.HTTP_400_BAD_REQUEST, reason="Cannot edit id field.")

    event_dict = JSONParser().parse(request)

    try:
        check_event = event.objects.get(id=id)
        if field == "date":
            check_event.date = event_dict["date"]
            check_event.save()
        elif field == "location":
            check_event.location = event_dict["location"]
            check_event.save()
        elif field == "name":
            check_event.name = event_dict["name"]
            check_event.save()
        elif field == "description":
            check_event.description = event_dict["description"]
            check_event.save()
        elif field == "organization":
            check_event.organization = event_dict["organization"]
            check_event.save()
        else:
            return HttpResponse(status=status.HTTP_400_BAD_REQUEST, reason="Must enter valid field.")
        return HttpResponse(status=status.HTTP_200_OK, reason="Event updated.")
    except event.DoesNotExist:
        return HttpResponse(status=status.HTTP_404_NOT_FOUND, reason="Event does not exist.")

@csrf_exempt
def remove_event_by_id(request, id):
    if request.method != "DELETE":
        return HttpResponse(status=status.HTTP_400_BAD_REQUEST, reason="Must use DELETE method.")

    try:
        check_event = event.objects.get(id=id)
        check_event.delete()
        return HttpResponse(status=status.HTTP_200_OK, reason="Event removed from database.")
    except event.DoesNotExist:
        return HttpResponse(status=status.HTTP_404_NOT_FOUND, reason="Event does not exist.")
