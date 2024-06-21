from django.contrib.auth.views import LogoutView
from .views import UserRegistrationView, UserLoginView, UserProfileView, PetCreateView, PetProfileView
from django.urls import path

app_name = 'users'


urlpatterns = [
    path('login/', UserLoginView.as_view(), name='login'),
    path('registration/', UserRegistrationView.as_view(), name='registration'),
    path('logout/', LogoutView.as_view(next_page='/'), name='logout'),
    path('profile/', UserProfileView.as_view(), name='profile'),
    path('pet-create/', PetCreateView.as_view(), name='pet_create'),
    path('pet_profile/<int:pk>', PetProfileView.as_view(), name='pet_profile'),
]
