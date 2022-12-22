from appoitment.api.serializers import AppointmentSerializer
from appoitment.models import Appointment
from rest_framework.permissions import IsAuthenticated

from rest_framework.generics import ListAPIView





class AppoitmentListView(ListAPIView):
    model = Appointment
    serializer_class = AppointmentSerializer



    def get_queryset(self):
        queryset = Appointment.objects.all()

        return queryset





