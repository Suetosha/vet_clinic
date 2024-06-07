from .views import UserLoginView, UserRegistrationForm
from django.urls import path

app_name = 'users'


urlpatterns = [
    path('login/', UserLoginView.as_view(), name='login'),
    path('registration/', UserRegistrationForm.as_view(), name='registration'),
]
