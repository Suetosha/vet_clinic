from django.contrib.auth.views import LogoutView
from .views import UserRegistrationView, UserLoginView
from django.urls import path

app_name = 'users'


urlpatterns = [
    path('login/', UserLoginView.as_view(), name='login'),
    path('registration/', UserRegistrationView.as_view(), name='registration'),
    path('logout/', LogoutView.as_view(next_page='/'), name='logout'),
]
