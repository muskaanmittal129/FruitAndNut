from django.urls import path
from .. import views

urlpatterns = [
    path('Aicte-Approval-Letter/', views.AicteApprovalLetterView.as_view(), name='aicte_approval_letter'),
    path('download/', views.DownloadView.as_view(), name='download'),
    path('list-of-holidays/', views.ListOfHolidayView.as_view(), name='list_of_holiday'),
    path('mandatory-disclosure/', views.MandatoryDisclosureView.as_view(), name='mandatory_disclosure'),
    path('naac/', views.NaacView.as_view(), name='naac'),

]