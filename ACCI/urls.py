from django import urls
from django.conf.urls import url
from django.contrib import admin
from django.urls import path
from django.urls.conf import include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    url('home', include("acci_main.urls")),
    url('home', include("acci_main.dropdwonurls")),
    url('admin/', admin.site.urls),
]+ static(settings.MEDIA_URL , document_root=settings.MEDIA_ROOT)
