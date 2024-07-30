from rest_framework import serializers

from appoitment.models import Appointment, SaasEntreprise,  ModeleDocument




class AppointmentSerializer(serializers.ModelSerializer):

    class Meta:
        model = Appointment
        fields = '__all__'




class ModeleDocumentSerializer(serializers.ModelSerializer):
    class Meta:
        model = ModeleDocument
        fields = ['title', 'content',]





