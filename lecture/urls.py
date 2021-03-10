from django.urls import path
from django.contrib.auth.views import LogoutView

from .views import HomeView,appliedEvents

app_name = 'lecture_app'

urlpatterns = [
    # path('login/', login_view, name="login"),
    # path('logout/', LogoutView.as_view(template_name='logout.html'), name="logout"),
    path('', HomeView.as_view(), name='home'),
    path('appliedEvents/<int:username>/',appliedEvents,name="appliedEvents"),
    
]
