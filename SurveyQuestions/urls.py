from django.urls import path
from SurveyQuestions import views

urlpatterns = [
    path('', views.index, name='index'),
    path('survey/', views.survey, name='survey'),
]