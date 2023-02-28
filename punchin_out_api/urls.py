from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from .views import *

urlpatterns = [
    path('PunchIn/', ClockPunchInView.as_view()),
    path('PunchOut/', login),
]