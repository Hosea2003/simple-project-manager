from .models import *
from rest_framework import serializers

class ProjetSerializer(serializers.ModelSerializer):
    numero = serializers.ReadOnlyField()
    nom=serializers.ReadOnlyField()

    class Meta:
        model=Projet
        fields="__all__"

class Travail(serializers.ModelSerializer):
    projet=serializers.PrimaryKeyRelatedField(read_only=True)
    nom=serializers.ReadOnlyField()

    class Meta:
        model=Travail
        fields="__all__"