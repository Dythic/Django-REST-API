from django.conf import settings
from django.conf.urls import include, url, path
from django.contrib import admin

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    path('', include('myapi.urls')),
]

if settings.DEBUG:
    import debug_toolbar
    urlpatterns = [
        url(r'^__debug__/', include(debug_toolbar.urls)),
    ] + urlpatterns