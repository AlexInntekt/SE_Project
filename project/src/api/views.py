from django.shortcuts import render
from rest_framework import generics
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from database.models import LanguageStream, Subject, Faculty, Department, Professor, TeachingHour
from .serializers.list import *

class LanguageStreamView(generics.ListAPIView):

    response_list = []
    serializer_class = LanguageStreamSerializer
    queryset = LanguageStream.objects.all()

    def list(self, request, *args, **kwargs):

        queryset = LanguageStream.objects.all()
        
        self.response_list = self.serializer_class(queryset, many=True, context={'request':request}).data

        return Response(self.response_list, status=status.HTTP_200_OK)