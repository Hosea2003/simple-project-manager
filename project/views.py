from rest_framework.decorators import api_view
from .models import *
from .serializers import *
from rest_framework.response import Response
from django.shortcuts import get_object_or_404

# Create your views here.
@api_view(["GET"])
def get_projet(request):

    projet=Projet.objects.all()

    return Response(ProjetSerializer(projet, many=True).data)

@api_view(["POST"])
def create_projet(request):
    numero=request.data.get("numero", None)
    nom=request.data.get("nom", None)

    if not(numero or nom):
        return Response("Remplissez tous les champs")

    if Projet.objects.filter(numero=numero).exists():
        return Response("Code already exist")

    projet = Projet.objects.create(
        numero=numero,
        nom=nom
    )

    return Response(ProjetSerializer(projet).data)

@api_view(["GET"])
def get_couple_bloc_tache(request, pk):
    
    # Projet avec id:pk
    projet=get_object_or_404(Projet, pk=pk)

    