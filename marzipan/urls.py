from django.conf.urls import url
from django.contrib import admin
from photogallery.views import *
urlpatterns = [
    url(r'^admin/', admin.site.urls),
]
