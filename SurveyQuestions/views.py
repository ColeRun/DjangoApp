from django.shortcuts import render
from .models import Survey, Question, Answer
from django.contrib.auth.decorators import login_required

# Create your views here.
#call survey template one

def index(request):
    return render(request, 'home1.html')

@login_required
def createsurvey(request):
    if request.method == 'POST':
        survey = Survey(title=request.POST['title'], user=request.user)
        survey.save()
        print("survey created")
        for question_text in request.POST.getlist('questions'):
            question = Question(text=question_text, survey=survey)
            question.save()
            print("question created")
            for answer_text in request.POST.getlist('answers'):
                answer = Answer(text=answer_text, question=question)
                answer.save()
                print("answer created")
        return survey_detail(request, survey.pk)
    else:
        return render(request, 'create_survey.html')

def survey_detail(request, pk):
    try:
        survey = Survey.objects.get(pk=pk)
        questions = Question.objects.filter(survey=survey)
        return render(request, 'survey_detail.html', {'survey': survey, 'questions': questions})
    except Survey.DoesNotExist:
        return render(request, 'survey_not_found.html')
    
    #recreate create survey template to be able to take variables "questions", "answers" and "survey" if user clicks edit survey.