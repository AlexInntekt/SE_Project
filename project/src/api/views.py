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



class SubjectView(generics.ListAPIView):

    response_list = []
    serializer_class = SubjectSerializer
    queryset = Subject.objects.all()

    def list(self, request, *args, **kwargs):

        queryset = Subject.objects.all()
        
        self.response_list = self.serializer_class(queryset, many=True, context={'request':request}).data

        return Response(self.response_list, status=status.HTTP_200_OK)



class FacultyView(generics.ListAPIView):

    response_list = []
    serializer_class = FacultySerializer
    queryset = Faculty.objects.all()

    def list(self, request, *args, **kwargs):

        queryset = Faculty.objects.all()
        
        self.response_list = self.serializer_class(queryset, many=True, context={'request':request}).data

        return Response(self.response_list, status=status.HTTP_200_OK)




class DepartmentView(generics.ListAPIView):

    response_list = []
    serializer_class = DepartmentSerializer
    queryset = Department.objects.all()

    def list(self, request, *args, **kwargs):

        queryset = Department.objects.all()
        
        self.response_list = self.serializer_class(queryset, many=True, context={'request':request}).data

        return Response(self.response_list, status=status.HTTP_200_OK)



class ProfessorView(generics.ListAPIView):

    response_list = []
    serializer_class = ProfessorSerializer
    queryset = Professor.objects.all()

    def list(self, request, *args, **kwargs):

        queryset = Professor.objects.all()
        
        self.response_list = self.serializer_class(queryset, many=True, context={'request':request}).data

        return Response(self.response_list, status=status.HTTP_200_OK)


class TeachingHourView(generics.ListAPIView):

    response_list = []
    serializer_class = TeachingHourSerializer
    queryset = TeachingHour.objects.all()

    def list(self, request, *args, **kwargs):

        queryset = TeachingHour.objects.all()
        
        self.response_list = self.serializer_class(queryset, many=True, context={'request':request}).data

        return Response(self.response_list, status=status.HTTP_200_OK)










class AddLanguageStreamView(generics.CreateAPIView):

	serializer_class = LanguageStreamSerializer


class AddSubjectView(generics.CreateAPIView):

	serializer_class = SubjectSerializer


class AddFacultyView(generics.CreateAPIView):

	serializer_class = FacultySerializer


class AddDepartmentView(generics.CreateAPIView):

	serializer_class = DepartmentSerializer


class AddProfessorView(generics.CreateAPIView):

	serializer_class = ProfessorSerializer


class AddTeachingHourView(generics.CreateAPIView):

	serializer_class = TeachingHourSerializer
