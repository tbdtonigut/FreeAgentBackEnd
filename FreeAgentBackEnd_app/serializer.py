from rest_framework import serializers
from FreeAgentBackEnd_app.models import Equipo
from FreeAgentBackEnd_app.models import Jugador
from FreeAgentBackEnd_app.models import Juego
from FreeAgentBackEnd_app.models import Oferta
from FreeAgentBackEnd_app.models import Cuota
from FreeAgentBackEnd_app.models import Torneo


class EquipoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Equipo
        fields = '__all__'


class JugadorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Jugador
        fields = '__all__'


class JuegoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Juego
        fields = '__all__'


class OfertaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Oferta
        fields = '__all__'


class CuotaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cuota
        fields = '__all__'


class TorneoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Torneo
        fields = '__all__'
