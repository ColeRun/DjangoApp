from django.urls import path
from SurveyQuestions import views

urlpatterns = [
    #create a path to the index view using index.html
    path('', views.createsurvey, name='createsurvey'),
    path('createsurvey', views.createsurvey, name='createsurvey'),
    path('editsurvey/<int:pk>', views.editsurvey, name='editsurvey'),
    path('survey_detail/<int:pk>', views.take_survey, name='take_survey'),
    path('user_surveys', views.user_surveys, name='user_surveys'),
    path('take_survey/<int:survey_id>', views.take_survey, name='take_survey'),
    path('preview_survey/<int:pk>', views.preview_survey, name='preview_survey'),
    path('/take_survey/review/<int:survey_id>/', views.review, name='review'),
    path('taker_survey_view', views.taker_survey_view, name='taker_survey_view'),

]

