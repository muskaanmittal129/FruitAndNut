from django.urls import path
from .. import views

urlpatterns = [
    path('center-of-excellence/', views.CenterOfExcView.as_view(), name='center_of_exc'),
    path('conferences/', views.ConferencesView.as_view(), name='conferences'),
    path('international-journal/', views.InternationalJournalView.as_view(), name='international_journal'),
    path('research-and-industrial/', views.ResearchAndIndustrialView.as_view(), name='research_and_industrial'),
]