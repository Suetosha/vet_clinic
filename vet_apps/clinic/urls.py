from django.urls import path, re_path
from vet_apps.clinic.views import (HomeTemplateView, DoctorsTemplateView, AppointmentCreateView,
                                   AppointmentSlotsCreateView, DoctorInfoTemplateView, DoctorAppointmentsView)


app_name = 'clinic'

urlpatterns = [
    path("", HomeTemplateView.as_view(), name='home'),
    path("doctors/", DoctorsTemplateView.as_view(), name='doctors'),
    path('doctor_info/<int:pk>', DoctorInfoTemplateView.as_view(), name='doctor_info'),
    re_path('doctor_appointments/(?P<selected_date>\d{4}-\d{2}-\d{2})?',
            DoctorAppointmentsView.as_view(), name='doctor_appointments'),
    path("appointment/", AppointmentCreateView.as_view(), name='appointment'),
    path("appointment_slots/", AppointmentSlotsCreateView.as_view(), name='appointment_slots'),

]