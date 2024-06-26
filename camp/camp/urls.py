from django.contrib import admin
from django.urls import path, include
from . import views
from django.conf.urls.static import static 
from django.conf import settings 

urlpatterns = [
    path('', include("camp_app.urls")),
    path('admin/', admin.site.urls),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) 

#Modify Site Header
admin.site.site_header = 'XYZ Camp'
#Modify Site Title
admin.site.site_title = 'XYZ Camp Site'