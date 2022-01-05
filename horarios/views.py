from django.shortcuts import render

from django.http import HttpResponse, JsonResponse
from rest_framework import serializers

from rest_framework.parsers import JSONParser
# from django.views.decorators.csrf import csrf_exempt

from horarios.models import Docente
from horarios.serializers import DocenteSerializer

from rest_framework.views import APIView

from rest_framework import mixins
from rest_framework import generics


# Create your views here.

class DocenteList(generics.ListCreateAPIView):
    queryset = Docente.objects.all()
    serializer_class = DocenteSerializer    

    # def get(self, request, *args, **kwargs):
    #     return self.list(request, *args, **kwargs)

    # def post(self, request, *args, **kwargs):
    #     return self.create(request, *args, **kwargs) 

class DocenteDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Docente.objects.all()
    serializer_class = DocenteSerializer

    # def get(self, request, *args, **kwargs):
    #     return self.retrieve(request, *args, **kwargs)

    # def put(self, request, *args, **kwargs):
    #     return self.update(request, *args, **kwargs)

    # def delete(self, request, *args, **kwargs):
    #     return self.destroy(request, *args, **kwargs)