from django.urls import path
from FreeAgentBackEnd_app.views import JugadorList, JugadorDetail, EquipoList, EquipoDetail, JuegoList, JuegoDetail, \
    OfertaList, OfertaDetail, TorneoList, TorneoDetail, CuotaList, CuotaDetail, JugadorByEquipo, login

urlpatterns = [
    path('v1/login/', login, name='Login'),
    path('v1/equipo/', EquipoList.as_view(), name='Equipo List'),
    path('v1/equipo/<int:pk>', EquipoDetail.as_view(), name="Equipo Detail"),
    path('v1/jugador/', JugadorList.as_view(), name='Jugador List'),
    path('v1/jugador/<int:pk>', JugadorDetail.as_view(), name="Jugador Detail"),
    path('v1/oferta/', OfertaList.as_view(), name='Oferta List'),
    path('v1/oferta/<int:pk>', OfertaDetail.as_view(), name="Oferta Detail"),
    path('v1/cuota/', CuotaList.as_view(), name='Cuota List'),
    path('v1/cuota/<int:pk>', CuotaDetail.as_view(), name="Cuota Detail"),
    path('v1/torneo/', TorneoList.as_view(), name='Torneo List'),
    path('v1/torneo/<int:pk>', TorneoDetail.as_view(), name="Torneo Detail"),
    path('v1/juego/', JuegoList.as_view(), name='Juego List'),
    path('v1/juego/<int:pk>', JuegoDetail.as_view(), name="Juego Detail"),
    path('v1/jugadorByEquipo/<int:pk>', JugadorByEquipo.as_view(), name='JugadorByEquipo List'),
]


