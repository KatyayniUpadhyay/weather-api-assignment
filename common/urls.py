from django.urls import path
from . import views
urlpatterns = [
    path("getCurrentWeather",views.GetCurrentWeather.as_view(), name="get_current_weather"),
]
