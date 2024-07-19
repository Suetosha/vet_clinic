from django.urls import path
from vet_apps.clinic.views import (HomeTemplateView, AboutUsTemplateView, AppointmentCreateView,
                                   AppointmentSlotsCreateView)


app_name = 'clinic'

urlpatterns = [
    path("", HomeTemplateView.as_view(), name='home'),
    path("about/", AboutUsTemplateView.as_view(), name='about'),
    path("appointment/", AppointmentCreateView.as_view(), name='appointment'),
    path("appointment_slots/", AppointmentSlotsCreateView.as_view(), name='appointment_slots'),

]