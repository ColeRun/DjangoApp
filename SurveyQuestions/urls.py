from django.urls import path
from SurveyQuestions import views

urlpatterns = [
    #create a path to the index view using index.html
    path('', views.createsurvey, name='createsurvey'),
    path('createsurvey', views.createsurvey, name='createsurvey'),
    path('editsurvey/<int:pk>', views.editsurvey, name='editsurvey'),
    path('survey_detail/<int:pk>', views.survey_detail, name='survey_detail'),
    path('user_surveys', views.user_surveys, name='user_surveys'),
   
]