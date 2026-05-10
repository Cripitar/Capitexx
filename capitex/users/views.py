from django.contrib.auth.models import User

from rest_framework import generics
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated

from .serializers import RegistroSerializer


class RegistroView(generics.CreateAPIView):

    queryset = User.objects.all()
    serializer_class = RegistroSerializer


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def perfil_usuario(request):

    usuario = request.user

    return Response({
        'id': usuario.id,
        'username': usuario.username,
        'email': usuario.email,
        'is_active': usuario.is_active,
    })


    