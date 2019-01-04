from django.urls import path
from .. import views

urlpatterns = [
    path('alumni/', views.TestimonialView.as_view(), name='testimonial'),
]