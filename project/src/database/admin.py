from django.contrib import admin

from .models import Subject, Professor, LanguageStream, Faculty, Department

admin.site.register(Subject)
admin.site.register(Professor)
admin.site.register(LanguageStream)
admin.site.register(Faculty)
admin.site.register(Department)