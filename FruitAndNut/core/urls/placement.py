from django.urls import path
from .. import views

urlpatterns = [
    path('placement-record/', views.PlacementRecordView.as_view(), name='placement_record'),
    path('recruitors/', views.RecruitorView.as_view(), name='recruitors'),
    path('tnp-cell/', views.TNPCellView.as_view(), name='tnp_cell'),
]