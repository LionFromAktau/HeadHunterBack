from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.viewsets import ViewSet, ModelViewSet
from . import models,serializers

class CustomUserView(ModelViewSet):
    def create_user(self, request, *args, **kwargs):
        serializer = serializers.CustomUserSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        models.CustomUser.objects.create_user(**serializer.validated_data)
        return Response(serializer.validated_data)