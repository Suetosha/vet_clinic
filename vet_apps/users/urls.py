from django.contrib.auth.views import LogoutView
from .views import UserRegistrationView, UserLoginView, UserProfileView, PetCreateView, PetProfileView, PetDeleteView, \
    DoctorProfileView
from django.urls import path, re_path

app_name = 'users'

urlpatterns = [
    path('login/', UserLoginView.as_view(), name='login'),
    path('registration/', UserRegistrationView.as_view(), name='registration'),
    path('logout/', LogoutView.as_view(next_page='/'), name='logout'),
    path('profile/', UserProfileView.as_view(), name='profile'),
    re_path('doctor_profile/', DoctorProfileView.as_view(), name='doctor_profile'),
    path('pet_create/', PetCreateView.as_view(), name='pet_create'),
    path('pet_delete/<int:pk>', PetDeleteView.as_view(), name='pet_delete'),
    path('pet_profile/<int:pk>', PetProfileView.as_view(), name='pet_profile'),

]
