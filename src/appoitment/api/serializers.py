from rest_framework import serializers

from appoitment.models import Appointment




class AppointmentSerializer(serializers.ModelSerializer):

    class Meta:
        model = Appointment
        fields = '__all__'




