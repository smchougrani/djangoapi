from django.urls import path

from appoitment.api.views import AppointmentListView



app_name = 'appoitment_api'


urlpatterns = [

    path('listappoitment/', AppointmentListView.as_view(), name='list_appointments'),


]



