from django.urls import path

from appoitment.api.views import AppointmentListView, create_demande_soin



app_name = 'appoitment_api'


urlpatterns = [

    path('listappoitment/', AppointmentListView.as_view(), name='list_appointments'),

    path('createdemande/', create_demande_soin, name='create_demande'),


]



