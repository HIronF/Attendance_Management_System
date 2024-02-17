from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path

from student_management_app import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('demo/', views.demo),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
