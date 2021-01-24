from django.urls import path

from .views import *

urlpatterns = [
path('v1/languages', LanguageStreamView.as_view())
]