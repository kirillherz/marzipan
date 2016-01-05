from django.conf.urls import url
from django.contrib import admin
from photogallery.views import *
from django.conf.urls.static import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from .settings import MEDIA_ROOT,MEDIA_URL

urlpatterns = [
    url(r'^admin/', admin.site.urls),
	url(r'^cakes/',listing_cakes),
]

urlpatterns += static(MEDIA_URL, document_root=MEDIA_ROOT)
urlpatterns += staticfiles_urlpatterns()