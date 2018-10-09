from django.urls import path
from .. import views

urlpatterns = [
    path('alumni/', views.AlumniView.as_view(), name='alumni'),
]