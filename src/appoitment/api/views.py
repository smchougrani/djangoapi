from appoitment.api.serializers import AppointmentSerializer
from appoitment.models import Appointment
from rest_framework.permissions import IsAuthenticated

from rest_framework.generics import ListAPIView






class AppointmentListView(ListAPIView):
    queryset = Appointment.objects.all()
    serializer_class = AppointmentSerializer

    def get_queryset(self):
        queryset = super().get_queryset()
        for appointment in queryset:
            appointment.decrypt_fields()
        return queryset





