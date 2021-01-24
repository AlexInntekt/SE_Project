from django.urls import path

from .views import *

urlpatterns = [
path('v1/languages', LanguageStreamView.as_view()),
path('v1/subjects', SubjectView.as_view()),
path('v1/faculties', FacultyView.as_view()),
path('v1/departments', DepartmentView.as_view()),
path('v1/professors', ProfessorView.as_view()),
path('v1/teaching_hours', TeachingHourView.as_view()),

path('v1/add_language', AddLanguageStreamView.as_view()),
path('v1/add_subject', AddSubjectView.as_view()),
path('v1/add_faculty', AddFacultyView.as_view()),
path('v1/add_department', AddDepartmentView.as_view()),
path('v1/add_professor', AddProfessorView.as_view()),
path('v1/add_teaching_hour', AddTeachingHourView.as_view()),
]