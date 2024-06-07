from django.urls import path
from vet_apps.clinic.views import HomeTemplateView, AboutUsTemplateView, AppointmentTemplateView

app_name = 'clinic'

urlpatterns = [
    path("", HomeTemplateView.as_view(), name='home'),
    path("about/", AboutUsTemplateView.as_view(), name='about'),
    path("appointment/", AppointmentTemplateView.as_view(), name='appointment'),
]