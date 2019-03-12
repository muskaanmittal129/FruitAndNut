from django.urls import path
from .. import views

urlpatterns = [
    path('event/', views.EventView.as_view(), name='event'),
    path('hostel/', views.HostelView.as_view(), name='hostel'),
    path('mediclaim/', views.MediclaimView.as_view(), name='mediclaim'),
    path('social_responsibility/', views.SocialResponsibilityView.as_view(), name='social_responsibility'),
    path('society/', views.SocietyView.as_view(), name='society'),
]
