from django.urls import path
from django.contrib.auth.views import LogoutView

from .views import HomeView, EventView, applied_events, past_events, upcoming_events, event_registration_view

app_name = "lecture_app"

urlpatterns = [
    path("", HomeView.as_view(), name="home"),
    path("applied_events/<int:user_pk>/", applied_events, name="applied_events"),
    path("upcoming_events/<int:user_pk>/", upcoming_events, name="upcoming_events"),
    path("past_events/<int:user_pk>/", past_events, name="past_events"),
    path("<int:user_pk>/event/<int:pk>/", EventView.as_view(), name="event"),
    path("<int:user_pk>/event/<int:pk>/register", event_registration_view, name="event_registration"),
]
