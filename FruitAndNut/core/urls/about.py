from django.urls import path
from .. import views

urlpatterns = [
    path('faculty/', views.FacultyView.as_view(), name='faculty'),
    path('labs',views.LabView.as_view(),name='lab'),
    path('gallery/',views.GalleryView.as_view(),name='gallery'),
    path('faculty_incentive/',views.FacultyIncentiveView.as_view(),name='faculty_incentive'),
    path('important_functionary/',views.ImportantFunctionaryView.as_view(),name='imp_functionary'),
    path('organization_chart/',views.OrganizationChartView.as_view(),name='organization_chart'),
    path('principal/',views.PrincipalView.as_view(),name='principal'),
    path('vision_and_mission/',views.VisionMissionView.as_view(),name='vision_and_mission'),
    path('infrastructure/',views.InfrastructureView.as_view(),name='infrastructure'),

]
