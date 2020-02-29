from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
import api.views as views


urlpatterns = [
    path("add-admin/", views.add_admin),
    path("get-all-admins/", views.get_all_admins)
]

urlpatterns = format_suffix_patterns(urlpatterns)
