from django.urls import path
from django.contrib.auth.views import LogoutView

from .views import HomeView, EventView, appliedEvents, pastEvents, upcomingEvents, eventRegistrationView

app_name = "lecture_app"

urlpatterns = [
    # path('login/', login_view, name="login"),
    # path('logout/', LogoutView.as_view(template_name='logout.html'), name="logout"),
    path("", HomeView.as_view(), name="home"),
    path("appliedEvents/<int:user_pk>/", appliedEvents, name="appliedEvents"),
    path("upcomingEvents/<int:user_pk>/", upcomingEvents, name="upcomingEvents"),
    path("pastEvents/<int:user_pk>/", pastEvents, name="pastEvents"),
    path("<int:user_pk>/event/<int:pk>/", EventView.as_view(), name="event"),
    path("<int:user_pk>/event/<int:pk>/register", eventRegistrationView, name="event_registration"),
]
