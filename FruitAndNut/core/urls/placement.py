from django.urls import path
from .. import views

urlpatterns = [
    path('placement-record/', views.PlacementRecordView.as_view(), name='placement_record'),
    path('recruitors/', views.RecruiterView.as_view(), name='recruitors'),
    path('tnp-cell/', views.TrainingPlacemenTDepartmentView.as_view(), name='tnp_cell'),
]
