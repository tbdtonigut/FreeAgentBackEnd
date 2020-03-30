from django.views.decorators.csrf import csrf_exempt
from rest_framework import generics
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.decorators import api_view, permission_classes
from rest_framework.pagination import PageNumberPagination
from rest_framework.authtoken.models import Token
from rest_framework.response import Response
from rest_framework.status import HTTP_400_BAD_REQUEST, HTTP_404_NOT_FOUND, HTTP_200_OK
from rest_framework.views import APIView
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated, AllowAny

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
@csrf_exempt
@api_view(["POST"])
@permission_classes((AllowAny,))
def login(request):
    email = request.data.get("email")
    password = request.data.get("password")
    if email is None or password is None:
        return Response({'error': 'Please provide both username and password'},
                        status=HTTP_400_BAD_REQUEST)
    user = Jugador.jugadores.filter(email=email, password=password).exists()
    if not user:
        return Response({'error': 'Invalid Credentials'},
                        status=HTTP_404_NOT_FOUND)
    token, _ = Token.objects.get_or_create(user=user)
    return Response({'token': token.key},
                    status=HTTP_200_OK)


class MyPagination(PageNumberPagination):
    page_size_query_param = 'page_size'


class EquipoList(generics.ListCreateAPIView):
    queryset = Equipo.equipos.all()
    serializer_class = EquipoSerializer
    pagination_class = MyPagination
    permission_classes = (IsAuthenticated,)
    authentication_classes = (TokenAuthentication,)

class EquipoDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Equipo.equipos.all()
    serializer_class = EquipoSerializer
    pagination_class = MyPagination
    permission_classes = (IsAuthenticated,)
    authentication_classes = (TokenAuthentication,)


class JugadorList(generics.ListCreateAPIView):
    queryset = Jugador.jugadores.all()
    serializer_class = JugadorSerializer
    pagination_class = MyPagination
    permission_classes = (IsAuthenticated,)
    authentication_classes = (TokenAuthentication,)


class JugadorDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Jugador.jugadores.all()
    serializer_class = JugadorSerializer
    pagination_class = MyPagination
    permission_classes = (IsAuthenticated,)


class JuegoList(generics.ListCreateAPIView):
    queryset = Juego.juegos.all()
    serializer_class = JuegoSerializer
    pagination_class = MyPagination
    permission_classes = (IsAuthenticated,)
    authentication_classes = (TokenAuthentication,)


class JuegoDetail(generics.RetrieveUpdateAPIView):
    queryset = Juego.juegos.all()
    serializer_class = JuegoSerializer
    pagination_class = MyPagination
    permission_classes = (IsAuthenticated,)
    authentication_classes = (TokenAuthentication,)


class OfertaList(generics.ListCreateAPIView):
    queryset = Oferta.ofertas.all()
    serializer_class = OfertaSerializer
    pagination_class = MyPagination
    permission_classes = (IsAuthenticated,)


class OfertaDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Oferta.ofertas.all()
    serializer_class = OfertaSerializer
    pagination_class = MyPagination
    permission_classes = (IsAuthenticated,)
    authentication_classes = (TokenAuthentication,)


class TorneoList(generics.ListCreateAPIView):
    queryset = Torneo.torneos.all()
    serializer_class = TorneoSerializer
    pagination_class = MyPagination
    permission_classes = (IsAuthenticated,)


class TorneoDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Torneo.torneos.all()
    serializer_class = TorneoSerializer
    pagination_class = MyPagination
    permission_classes = (IsAuthenticated,)
    authentication_classes = (TokenAuthentication,)


class CuotaList(generics.ListCreateAPIView):
    queryset = Cuota.cuotas.all()
    serializer_class = CuotaSerializer
    pagination_class = MyPagination
    permission_classes = (IsAuthenticated,)
    authentication_classes = (TokenAuthentication,)


class CuotaDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Cuota.cuotas.all()
    serializer_class = CuotaSerializer
    pagination_class = MyPagination
    permission_classes = (IsAuthenticated,)
    authentication_classes = (TokenAuthentication,)


# --------------------------------------------------- Consultas especiales

class JugadorByEquipo(generics.ListAPIView):
    def get_queryset(self):
        queryset = Jugador.jugadores.filter(equipo_id=self.kwargs['pk'])
        return queryset

    serializer_class = JugadorSerializer
    pagination_class = None
    permission_classes = (IsAuthenticated,)
    authentication_classes = (TokenAuthentication,)
