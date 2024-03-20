from django.urls import path
from SurveyQuestions import views

urlpatterns = [
    #create a path to the index view using index.html
    path('', views.index, name='index'),
    path('createsurvey', views.createsurvey, name='createsurvey'),
   
]