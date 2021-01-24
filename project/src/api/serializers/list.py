from rest_framework import serializers
from django.db import models
from django.core.exceptions import ObjectDoesNotExist

from database.models import LanguageStream, Subject, Faculty, Department, Professor, TeachingHour


class LanguageStreamSerializer(serializers.ModelSerializer):

    class Meta:
        model = LanguageStream
        fields = '__all__'


class SubjectSerializer(serializers.ModelSerializer):

    class Meta:
        model = Subject
        fields = '__all__'


class FacultySerializer(serializers.ModelSerializer):

    class Meta:
        model = Faculty
        fields = '__all__'


class DepartmentSerializer(serializers.ModelSerializer):

    class Meta:
        model = Department
        fields = '__all__'


class DepartmentSerializer(serializers.ModelSerializer):

    class Meta:
        model = Department
        fields = '__all__'


class ProfessorSerializer(serializers.ModelSerializer):

    class Meta:
        model = Professor
        fields = '__all__'


class TeachingHourSerializer(serializers.ModelSerializer):

    class Meta:
        model = TeachingHour
        fields = '__all__'