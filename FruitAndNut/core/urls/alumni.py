from django.urls import path
from .. import views

urlpatterns = [
    path('testimonials/', views.TestimonialView.as_view(), name='testimonial'),
    path('our_alumni/', views.AlumniView.as_view(), name ='alumni')
]
