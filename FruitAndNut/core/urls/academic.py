from django.urls import path
from .. import views

urlpatterns = [
    path('time-table/', views.TimeTableView.as_view(), name='time_table'),
    path('academic-calender/', views.AcademicCalendarView.as_view(), name='calender'),
    path('syllabus/', views.SyllabusView.as_view(), name='syllabus'),
    path('awards/', views.AwardsListView.as_view(), name = 'awards_list'),
    path('college_award_session/', views.CollegeAwardsListView.as_view(), name ='colg_award_list'),
    path('college_awards/<session>/', views.UniversityAwardsView.as_view(), name = 'uni_awards'),
    path('univeristy_awards/<session>/', views.CollegeAwardView.as_view(), name = 'colg_awards'),
    path('affiliation/', views.AffiliationView.as_view(), name='affiliation'),
]