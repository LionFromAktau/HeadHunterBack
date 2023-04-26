from asgiref.sync import async_to_sync
from channels.layers import get_channel_layer
from django.dispatch import Signal, receiver
from . import models, serializers

vacancy_submitted =  Signal()

@receiver(vacancy_submitted)
def send_vacancy_noticification(sender, **kwargs):
    channel_layer = get_channel_layer()
    serializer = serializers.VacancySerializerV1(kwargs['instance'])
    async_to_sync(channel_layer.group_send)(
        'submitted',
        {
            'type': 'send_noticification',
            **serializer.data,
        }
    )