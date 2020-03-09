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
        return HttpResponse(status=status.HTTP_302_FOUND, reason="Admin account already exists.")
    except admin.DoesNotExist:
        new_admin = admin_serializer(data=admin_dict)
        if new_admin.is_valid():
            new_admin.save()
            return HttpResponse(status=status.HTTP_201_CREATED, reason="New admin created.")
        else:
            return HttpResponse(status=status.HTTP_400_BAD_REQUEST, reason="Object was not in a valid form.")
    except KeyError:
        return HttpResponse(status=status.HTTP_400_BAD_REQUEST, reason="Object was not in a valid form.")

@csrf_exempt
def validate_admin(request):
    if request.method != "POST":
        return HttpResponse(status=status.HTTP_400_BAD_REQUEST, reason="Must use POST method.")

    admin_dict = JSONParser().parse(request)

    try:
        check_admin = admin.objects.get(username=admin_dict["username"], passwd=admin_dict["passwd"])
        return HttpResponse(status=status.HTTP_200_OK, reason="Login successful.")
    except admin.DoesNotExist:
        return HttpResponse(status=status.HTTP_404_NOT_FOUND, reason="Admin doesn't exist or password is incorrect.")
    except KeyError:
        return HttpResponse(status=status.HTTP_400_BAD_REQUEST, reason="Object was not in a valid form.")

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
    except KeyError:
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

    check_announcements = announcement.objects.all().distinct().order_by("-authored_date")
    announcements_dict = announcement_serializer(check_announcements, many=True)
    return JsonResponse(announcements_dict.data, safe=False)

@csrf_exempt
def edit_announcement_by_id(request, id):
    if request.method != "POST":
        return HttpResponse(status=status.HTTP_400_BAD_REQUEST, reason="Must use POST method.")

    announcement_dict = JSONParser().parse(request)

    try:
        check_announcement = announcement.objects.get(id=id)
        check_announcement.author = announcement_dict["author"]
        check_announcement.authored_date = announcement_dict["authored_date"]
        check_announcement.description = announcement_dict["description"]
        check_announcement.subject = announcement_dict["subject"]
        check_announcement.save()
        return HttpResponse(status=status.HTTP_200_OK, reason="Announcement updated.")
    except announcement.DoesNotExist:
        return HttpResponse(status=status.HTTP_404_NOT_FOUND, reason="Announcement does not exist.")
    except KeyError:
        return HttpResponse(status=status.HTTP_400_BAD_REQUEST, reason="Object was not in a valid form.")

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
            return HttpResponse(status=status.HTTP_400_BAD_REQUEST, reason="Object was not in a valid form.")
    except KeyError:
        return HttpResponse(status=status.HTTP_400_BAD_REQUEST, reason="Object was not in a valid form.")

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

    check_events = event.objects.all().distinct().order_by("-date")
    events_dict = event_serializer(check_events, many=True)
    return JsonResponse(events_dict.data, safe=False)

@csrf_exempt
def edit_event_by_id(request, id):
    if request.method != "POST":
        return HttpResponse(status=status.HTTP_400_BAD_REQUEST, reason="Must use POST method.")

    event_dict = JSONParser().parse(request)

    try:
        check_event = event.objects.get(id=id)
        check_event.date = event_dict["date"]
        check_event.description = event_dict["description"]
        check_event.location = event_dict["location"]
        check_event.name = event_dict["name"]
        check_event.organization = event_dict["organization"]
        check_event.save()
        return HttpResponse(status=status.HTTP_200_OK, reason="Event updated.")
    except event.DoesNotExist:
        return HttpResponse(status=status.HTTP_404_NOT_FOUND, reason="Event does not exist.")
    except KeyError:
        return HttpResponse(status=status.HTTP_400_BAD_REQUEST, reason="Object was not in a valid form.")

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

@csrf_exempt
def add_article(request):
    if request.method != "POST":
        return HttpResponse(status=status.HTTP_400_BAD_REQUEST, reason="Must use POST method.")

    article_dict = JSONParser().parse(request)

    try:
        check_article = article.objects.get(subject=article_dict["subject"])
        return HttpResponse(status=status.HTTP_302_FOUND, reason="Article already exists.")
    except article.DoesNotExist:
        new_article = article_serializer(data=article_dict)
        if new_article.is_valid():
            new_article.save()
            return HttpResponse(status=status.HTTP_201_CREATED, reason="New article created.")
        else:
            return HttpResponse(status=status.HTTP_400_BAD_REQUEST, reason="Object was not in a valid form.")
    except KeyError:
        return HttpResponse(status=status.HTTP_400_BAD_REQUEST, reason="Object was not in a valid form.")

@csrf_exempt
def get_article_by_id(request, id):
    if request.method != "GET":
        return HttpResponse(status=status.HTTP_400_BAD_REQUEST, reason="Must use GET method.")

    try:
        check_article = article.objects.get(id=id)
        article_dict = article_serializer(check_article)
        return JsonResponse(article_dict.data)
    except article.DoesNotExist:
        return HttpResponse(status=status.HTTP_404_NOT_FOUND, reason="Article does not exist.")

@csrf_exempt
def get_all_articles(request):
    if request.method != "GET":
        return HttpResponse(status=status.HTTP_400_BAD_REQUEST, reason="Must use GET method.")

    check_articles = article.objects.all().distinct().order_by("subject")
    articles_dict = article_serializer(check_articles, many=True)
    return JsonResponse(articles_dict.data, safe=False)

@csrf_exempt
def edit_article_by_id(request, id):
    if request.method != "POST":
        return HttpResponse(status=status.HTTP_400_BAD_REQUEST, reason="Must use POST method.")

    article_dict = JSONParser().parse(request)

    try:
        check_article = article.objects.get(id=id)
        check_article.subject = article_dict["subject"]
        check_article.description = article_dict["description"]
        check_article.save()
        return HttpResponse(status=status.HTTP_200_OK, reason="Article updated.")
    except article.DoesNotExist:
        return HttpResponse(status=status.HTTP_404_NOT_FOUND, reason="Article does not exist.")
    except KeyError:
        return HttpResponse(status=status.HTTP_400_BAD_REQUEST, reason="Object was not in a valid form.")

@csrf_exempt
def remove_article_by_id(request, id):
    if request.method != "DELETE":
        return HttpResponse(status=status.HTTP_400_BAD_REQUEST, reason="Must use DELETE method.")

    try:
        check_article = article.objects.get(id=id)
        check_article.delete()
        return HttpResponse(status=status.HTTP_200_OK, reason="Article removed from database.")
    except article.DoesNotExist:
        return HttpResponse(status=status.HTTP_404_NOT_FOUND, reason="Article does not exist.")

@csrf_exempt
def add_contact(request):
    if request.method != "POST":
        return HttpResponse(status=status.HTTP_400_BAD_REQUEST, reason="Must use POST method.")

    contact_dict = JSONParser().parse(request)

    try:
        check_contact = contact.objects.get(name=contact_dict["name"])
        return HttpResponse(status=status.HTTP_302_FOUND, reason="Contact already exists.")
    except contact.DoesNotExist:
        new_contact = contact_serializer(data=contact_dict)
        if new_contact.is_valid():
            new_contact.save()
            return HttpResponse(status=status.HTTP_201_CREATED, reason="New contact created.")
        else:
            return HttpResponse(status=status.HTTP_400_BAD_REQUEST, reason="Object was not in a valid form.")
    except KeyError:
        return HttpResponse(status=status.HTTP_400_BAD_REQUEST, reason="Object was not in a valid form.")

@csrf_exempt
def get_contact_by_id(request, id):
    if request.method != "GET":
        return HttpResponse(status=status.HTTP_400_BAD_REQUEST, reason="Must use GET method.")

    try:
        check_contact = contact.objects.get(id=id)
        contact_dict = contact_serializer(check_contact)
        return JsonResponse(contact_dict.data)
    except contact.DoesNotExist:
        return HttpResponse(status=status.HTTP_404_NOT_FOUND, reason="Contact does not exist.")

@csrf_exempt
def get_all_contacts(request):
    if request.method != "GET":
        return HttpResponse(status=status.HTTP_400_BAD_REQUEST, reason="Must use GET method.")

    check_contacts = contact.objects.all().distinct().order_by("name")
    contacts_dict = contact_serializer(check_contacts, many=True)
    return JsonResponse(contacts_dict.data, safe=False)

@csrf_exempt
def edit_contact_by_id(request, id):
    if request.method != "POST":
        return HttpResponse(status=status.HTTP_400_BAD_REQUEST, reason="Must use POST method.")

    contact_dict = JSONParser().parse(request)

    try:
        check_contact = contact.objects.get(id=id)
        check_contact.name = contact_dict["name"]
        check_contact.email = contact_dict["email"]
        check_contact.phone = contact_dict["phone"]
        check_contact.office = contact_dict["office"]
        check_contact.save()
        return HttpResponse(status=status.HTTP_200_OK, reason="Contact updated.")
    except contact.DoesNotExist:
        return HttpResponse(status=status.HTTP_404_NOT_FOUND, reason="Contact does not exist.")
    except KeyError:
        return HttpResponse(status=status.HTTP_400_BAD_REQUEST, reason="Object was not in a valid form.")

@csrf_exempt
def remove_contact_by_id(request, id):
    if request.method != "DELETE":
        return HttpResponse(status=status.HTTP_400_BAD_REQUEST, reason="Must use DELETE method.")

    try:
        check_contact = contact.objects.get(id=id)
        check_contact.delete()
        return HttpResponse(status=status.HTTP_200_OK, reason="Contact removed from database.")
    except contact.DoesNotExist:
        return HttpResponse(status=status.HTTP_404_NOT_FOUND, reason="Contact does not exist.")
