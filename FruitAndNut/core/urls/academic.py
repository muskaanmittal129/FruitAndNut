from django.urls import path
from .. import views

urlpatterns = [
    path('time-table/', views.TimeTableView.as_view(), name='time_table'),
    path('academic-calender/', views.AcademicCalendarView.as_view(), name='calender'),
    path('syllabus/', views.SyllabusView.as_view(), name='syllabus'),
    path('university_awards_list/', views.UniversityAwardsYearView.as_view(), name = 'awards_list'),
    path('college_awards_list/', views.CollegeAwardsYearView.as_view(), name ='colg_award_list'),
    path('univeristy_awards/<session>/', views.UniversityAwardsView.as_view(), name = 'uni_awards'),
    path('college_awards/<session>/', views.CollegeAwardsView.as_view(), name = 'college_awards'),
    path('affiliation/', views.AffiliationView.as_view(), name='affiliation'),
]
