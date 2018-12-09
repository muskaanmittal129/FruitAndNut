from django.urls import path
from .. import views

urlpatterns = [
    path('time-table/', views.TimeTableView.as_view(), name='time_table'),
    path('academic-calender/', views.AcademicCalendarView.as_view(), name='calender'),
    path('syllabus/', views.SyllabusView.as_view(), name='syllabus'),
    path('awards/', views.AwardsView.as_view(), name = 'awards_list'),
    path('univeristy_awards/<session>/', views.UniversityAwardsView.as_view(), name = 'uni_awards'),
    path('affiliation/', views.AffiliationView.as_view(), name='affiliation'),
]