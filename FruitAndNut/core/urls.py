from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from . import views

urlpatterns = [
    path('', views.Home.as_view(), name='home'),
    # path('',include('core.urls.about_urls')),
    path('faculty/', views.FacultyView.as_view(), name='faculty'),
    path('labs',views.LabView.as_view(),name='lab'),
    path('gallery/',views.GalleryView.as_view(),name='gallery'),
    path('important_functionary/',views.ImportantFunctionaryView.as_view(),name='imp_functionary'),
    path('organization_chart/',views.OrganizationChartView.as_view(),name='organization_chart'),
    path('principal/',views.PrincipalView.as_view(),name='principal'),
    path('alumni/',views.AlumniView.as_view(),name='alumni'),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
