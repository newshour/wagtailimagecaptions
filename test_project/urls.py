from django.contrib import admin
from django.urls import include, path

from wagtail import urls as wagtail_urls
from wagtail.admin import urls as wagtailadmin_urls

urlpatterns = [
    path("admin/", admin.site.urls),
    path("wagtail/", include(wagtailadmin_urls)),
    path("", include(wagtail_urls)),
]
