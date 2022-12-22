from django.urls import path

from appoitment.api.views import AppoitmentListView



app_name = 'appoitment_api'


urlpatterns = [

    path('listappoitment/', AppoitmentListView.as_view(), name='list_appointments'),


]



