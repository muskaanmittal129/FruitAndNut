from django.urls import path
from .. import views
from django.views.generic.base import TemplateView

urlpatterns = [
    path('event/', views.EventView.as_view(), name='event'),
    path('hostel/', views.HostelView.as_view(), name='hostel'),
    path('mediclaim/', views.MediclaimView.as_view(), name='mediclaim'),
    path('social_responsibility/Adarsh_Vikas_Kendra/', TemplateView.as_view(template_name='core/life_akgec/avk.htm'), name='avk'),
    path('social_responsibility/BDC/', TemplateView.as_view(template_name='core/life_akgec/BDC.htm'), name='BDC'),
    path('social_responsibility/environmental-sustenance-eco-friendliness/', TemplateView.as_view(template_name='core/life_akgec/Env_Eco.htm'), name='Env_Eco'),
    path('social_responsibility/sdpvss/', TemplateView.as_view(template_name='core/life_akgec/Skill_school.htm'), name='Skill_school'),
    path('social_responsibility/', views.SocialResponsibilityView.as_view(), name='social_responsibility'),
    path('society/', views.SocietyView.as_view(), name='society'),
]
