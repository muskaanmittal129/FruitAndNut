from django.urls import path, include
from .. import views

urlpatterns = [
    path('', views.Home.as_view(), name='home'),
    path('', include('core.urls.about')),
    path('', include('core.urls.academic')),
    path('', include('core.urls.r_and_d')),
    path('', include('core.urls.about')),
    path('', include('core.urls.life_akgec')),
    path('', include('core.urls.admission')),
    path('', include('core.urls.placement')),
    path('', include('core.urls.alumni')),
    path('', include('core.urls.quick_link')),
]