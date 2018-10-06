from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from . import views

urlpatterns = [
    path('', views.Home.as_view(), name='home'),
    path('faculty/', views.FacultyView.as_view(), name='faculty'),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)