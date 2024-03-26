from django.shortcuts import render
from .models import Survey, Question, Answer

# Create your views here.
#call survey template one
def index(request):
    return render(request, 'home1.html')

def createsurvey(request):
    if request.method == 'POST':
        survey = Survey(title=request.POST['title'], user=request.user)
        survey.save()
        for question_text in request.POST.getlist('questions'):
            question = Question(text=question_text, survey=survey)
            question.save()
            for answer_text in request.POST.getlist('answers'):
                answer = Answer(text=answer_text, question=question)
                answer.save()
        return render(request, 'survey_created.html')
    else:
        return render(request, 'create_survey.html')
    

def survey_detail(request, pk):
    survey = Survey.objects.get(pk=pk)
    questions = Question.objects.filter(survey=survey)
    return render(request, 'survey_detail.html', {'survey': survey, 'questions': questions})