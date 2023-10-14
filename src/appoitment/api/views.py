from appoitment.api.serializers import AppointmentSerializer
from appoitment.models import Appointment
from rest_framework.permissions import IsAuthenticated

from rest_framework.generics import ListAPIView



from channels.layers import get_channel_layer
from asgiref.sync import async_to_sync
from django.http import JsonResponse
from appoitment.models import DemandeSoin
from django.views.decorators.csrf import csrf_exempt
import time



# ExponentPushToken[rCcxM4B1mcbEU4U0Z-_3m4]
# ExponentPushToken[G51o7KNBgdtqigqTLVMBSw]

import requests



@csrf_exempt
def create_demande_soin(request):
    # Créer une nouvelle demande de soin (adaptez ceci selon vos besoins)
    demande = DemandeSoin(description="Description de la demande...")
    demande.save()

    # Liste des tokens pour les appareils cibles
    tokens = [
        "ExponentPushToken[rCcxM4B1mcbEU4U0Z-_3m4]",
        "ExponentPushToken[G51o7KNBgdtqigqTLVMBSw]",
        # Ajoutez d'autres tokens si nécessaire
    ]

    headers = {
        "Content-Type": "application/json",
        "Accept": "application/json"
    }

    success_count = 0
    for token in tokens:
        data = {
            "to": token,
            "title": "Nouvelle demande de soin",
            "body": "Nouvelle demande de soin créée!",
            "data": {"nom": "Mohammed salam"}
        }

        response = requests.post("https://exp.host/--/api/v2/push/send", headers=headers, json=data)

        # Vérifiez la réponse de l'API Expo pour chaque notification
        if response.status_code == 200:
            success_count += 1
        else:
            print(f"Failed for token {token} with response: {response.json()}")

    if success_count == len(tokens):
        return JsonResponse({"message": "Demande de soin créée et notifications envoyées avec succès à tous les utilisateurs."})
    else:
        return JsonResponse({"message": f"Demande de soin créée, mais échec de l'envoi de la notification à {len(tokens) - success_count} utilisateurs."})


# @csrf_exempt
# def create_demande_soin(request):
#     # Créer une nouvelle demande de soin (adaptez ceci selon vos besoins)
#     demande = DemandeSoin(description="Description de la demande...")
#     demande.save()

#     # Envoyer une notification via WebSocket
#     channel_layer = get_channel_layer()
#     async_to_sync(channel_layer.group_send)(
#         "notification_group",
#         {
#             'type': 'send_notification',
#             'message': 'Nouvelle demande de soin créée!'
#         }
#     )

#     return JsonResponse({"message": "Demande de soin créée avec succès."})



class AppointmentListView(ListAPIView):
    queryset = Appointment.objects.all()
    serializer_class = AppointmentSerializer

    def get_queryset(self):
        queryset = super().get_queryset()
        for appointment in queryset:
            appointment.decrypt_fields()
        return queryset





