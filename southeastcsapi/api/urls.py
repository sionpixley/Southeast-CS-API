from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
import api.views as views


urlpatterns = [
    path("add-admin/", views.add_admin),
    path("validate-admin/", views.validate_admin),
    path("get-all-admins/", views.get_all_admins),
    path("add-announcement/", views.add_announcement),
    path("get-announcement-by-id/<int:id>/", views.get_announcement_by_id),
    path("get-all-announcements/", views.get_all_announcements),
    path("edit-announcement-by-id/<int:id>/", views.edit_announcement_by_id),
    path("remove-announcement-by-id/<int:id>/", views.remove_announcement_by_id),
    path("add-event/", views.add_event),
    path("get-event-by-id/<int:id>/", views.get_event_by_id),
    path("get-all-events/", views.get_all_events),
    path("edit-event-by-id/<int:id>/", views.edit_event_by_id),
    path("remove-event-by-id/<int:id>/", views.remove_event_by_id),
    path("add-course/", views.add_course),
    path("get-course-by-id/<int:id>/", views.get_course_by_id),
    path("get-all-courses/", views.get_all_courses),
    path("edit-course-by-id/<int:id>/", views.edit_course_by_id),
    path("remove-course-by-id/<int:id>/", views.remove_course_by_id),
    path("add-contact/", views.add_contact),
    path("get-contact-by-id/<int:id>/", views.get_contact_by_id),
    path("get-all-contacts/", views.get_all_contacts),
    path("edit-contact-by-id/<int:id>/", views.edit_contact_by_id),
    path("remove-contact-by-id/<int:id>/", views.remove_contact_by_id)
]

urlpatterns = format_suffix_patterns(urlpatterns)
