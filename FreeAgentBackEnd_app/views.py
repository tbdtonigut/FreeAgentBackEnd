from django.contrib.auth import authenticate, login
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render
from django.urls import reverse
from rest_framework import generics
from rest_framework.pagination import PageNumberPagination

from .models import Equipo
from .serializer import EquipoSerializer
from .models import Jugador
from .serializer import JugadorSerializer
from .models import Juego
from .serializer import JuegoSerializer
from .models import Oferta
from .serializer import OfertaSerializer
from .models import Cuota
from .serializer import CuotaSerializer
from .models import Torneo
from .serializer import TorneoSerializer

# Create your views here.

class MyPagination(PageNumberPagination):
    page_size_query_param = 'page_size'


class EquipoList(generics.ListCreateAPIView):
    queryset = Equipo.equipos.all()
    serializer_class = EquipoSerializer
    pagination_class = MyPagination

class EquipoDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Equipo.equipos.all()
    serializer_class = EquipoSerializer
    pagination_class = MyPagination

class JugadorList(generics.ListCreateAPIView):
    queryset = Jugador.jugadores.all()
    serializer_class = JugadorSerializer
    pagination_class = MyPagination

class JugadorDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Jugador.jugadores.all()
    serializer_class = JugadorSerializer
    pagination_class = MyPagination

class JuegoList(generics.ListCreateAPIView):
    queryset = Juego.juegos.all()
    serializer_class = JuegoSerializer
    pagination_class = MyPagination

class JuegoDetail(generics.RetrieveUpdateAPIView):
    queryset = Juego.juegos.all()
    serializer_class = JuegoSerializer
    pagination_class = MyPagination

class OfertaList(generics.ListCreateAPIView):
    queryset = Oferta.ofertas.all()
    serializer_class = OfertaSerializer
    pagination_class = MyPagination

class OfertaDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Oferta.ofertas.all()
    serializer_class = OfertaSerializer
    pagination_class = MyPagination

class TorneoList(generics.ListCreateAPIView):
    queryset = Torneo.torneos.all()
    serializer_class = TorneoSerializer
    pagination_class = MyPagination

class TorneoDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Torneo.torneos.all()
    serializer_class = TorneoSerializer
    pagination_class = MyPagination

class CuotaList(generics.ListCreateAPIView):
    queryset = Cuota.cuotas.all()
    serializer_class = CuotaSerializer
    pagination_class = MyPagination

class CuotaDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Cuota.cuotas.all()
    serializer_class = CuotaSerializer
    pagination_class = MyPagination

#--------------------------------------------------- Consultas especiales

class JugadorByEquipo(generics.ListAPIView):
    def get_queryset(self):
        queryset = Jugador.jugadores.filter(equipo_id=self.kwargs['pk'])
        return queryset
    serializer_class = JugadorSerializer
    pagination_class = None

