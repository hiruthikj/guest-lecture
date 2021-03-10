from django.urls import path

from .views import SignUpView, login_view, CustomLogOutView

# app_name = 'accounts'

urlpatterns = [
    # path('signup/', SignUpView.as_view(), name='signup'),
    path('login/', login_view, name='login'),
    path('logout/', CustomLogOutView.as_view(), name='logout'),
]
