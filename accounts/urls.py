from django.urls import path
from django.views.generic.base import TemplateView

from .views import login_view, CustomLogOutView, signup_view

# app_name = 'accounts'

urlpatterns = [
    path('signup/', signup_view, name='signup'),
    path('signup-sucess/', TemplateView.as_view(template_name="signup_success.html"), name='signup_success'),
    path('login/', login_view, name='login'),
    path('logout/', CustomLogOutView.as_view(), name='logout'),
]
