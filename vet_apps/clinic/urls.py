from django.urls import path
from vet_apps.clinic.views import (HomeTemplateView, DoctorsTemplateView, AppointmentCreateView,
                                   AppointmentSlotsCreateView, DoctorInfoTemplateView)


app_name = 'clinic'

urlpatterns = [
    path("", HomeTemplateView.as_view(), name='home'),
    path("doctors/", DoctorsTemplateView.as_view(), name='doctors'),
    path('doctor_info/<int:pk>', DoctorInfoTemplateView.as_view(), name='doctor_info'),
    path("appointment/", AppointmentCreateView.as_view(), name='appointment'),
    path("appointment_slots/", AppointmentSlotsCreateView.as_view(), name='appointment_slots'),

]