from django.contrib import admin

from .models import Subject, Professor, LanguageStream

admin.site.register(Subject)
admin.site.register(Professor)
admin.site.register(LanguageStream)