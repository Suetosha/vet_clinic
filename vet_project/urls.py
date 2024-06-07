from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path('admin/', admin.site.urls),

    path('', include('vet_apps.clinic.urls')),
    path('users/', include('vet_apps.users.urls'))

]
