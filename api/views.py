from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Suscripcion
from rest_framework import status

# Create your views here.
@api_view(['GET'])
def suscrito(request, email):
    try:
        suscrito = Suscripcion.objects.get(usuario=email)
        suscrito.estado = True
        return Response({"suscrito": suscrito.estado}, status.HTTP_200_OK)
    except Suscripcion.DoesNotExist:
        return Response({"suscrito": False}, status.HTTP_200_OK)

@api_view(['GET'])
def suscribir(request, email):
    try:
        suscrito = Suscripcion.objects.get(usuario=email)
        suscrito.estado = True
        suscrito.save()
        return Response({"mensaje": "Se a renovado su suscripcion"}, status.HTTP_200_OK)
    except Suscripcion.DoesNotExist:
        suscrito = Suscripcion()
        suscrito.usuario = email
        suscrito.estado = True
        suscrito.save()
        return Response({"mensaje": "Su suscripción se a realizado con éxito."}, status.HTTP_200_OK)