from django.urls import path
from .. import views

urlpatterns = [
    path('time-table/', views.TimeTableView.as_view(), name='time_table'),
    path('academic-calender/', views.AcademicCalenderView.as_view(), name='calender'),
    path('syllabus/', views.SyllabusView.as_view(), name='syllabus'),
]