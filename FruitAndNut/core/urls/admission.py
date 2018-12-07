from django.urls import path
from .. import views

urlpatterns = [
    path('admission-process/', views.AdmissionProcessView.as_view(), name='admission_process'),
    path('fee-structure/', views.FeeStructureView.as_view(), name='fee_structure'),
    path('info-booklet/', views.InfoBookletView.as_view(), name='info_booklet'),
    path('refund-norms/', views.RefundNormsView.as_view(), name='refund_norms'),

]