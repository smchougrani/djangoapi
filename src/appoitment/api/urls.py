from django.urls import path

from appoitment.api.views import (AppointmentListView, create_demande_soin, submit_document,
                                    SaasEntrepriseDetailView , )



app_name = 'appoitment_api'


urlpatterns = [

    path('listappoitment/', AppointmentListView.as_view(), name='list_appointments'),

    path('createdemande/', create_demande_soin, name='create_demande'),
    path('submit_document/', submit_document, name='submit_document'),
    path('doc/<int:id>/', SaasEntrepriseDetailView.as_view(), name='entreprise-detail'),

]



