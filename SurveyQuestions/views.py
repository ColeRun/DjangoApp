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
        questions = request.POST.getlist('questions')
        for i in range(len(questions)):
            question_text = questions[i]
            question = Question(text=question_text, survey=survey)
            question.save()
            print("question created")
            answers = request.POST.getlist('answers-' + str(i+1))
            for answer_text in answers:
                answer = Answer(text=answer_text, question=question)
                answer.save()
                print("answer created")
        return createdsurvey(request, survey.pk)
    return render(request, 'create_survey.html')

@login_required
def survey_detail(request, pk):
    try:
        survey = Survey.objects.get(pk=pk)
        questions = Question.objects.filter(survey=survey).prefetch_related('answer_set')
        return render(request, 'survey_detail.html', {'survey': survey, 'questions': questions})
    except Survey.DoesNotExist:
        return render(request, 'survey_not_found.html')
    

    
def user_surveys(request):
    surveys = Survey.objects.filter(user=request.user)
    return render(request, 'user_surveys.html', {'surveys': surveys})    

@login_required
def editsurvey(request, pk):
    try:
        survey = Survey.objects.get(pk=pk)
        questions = Question.objects.filter(survey=survey).prefetch_related('answer_set')
        return render(request, 'edit_survey.html', {'survey': survey, 'questions': questions})
    except Survey.DoesNotExist:
        return render(request, 'survey_not_found.html')

@login_required
def createdsurvey(request, pk):
    return render(request, 'create_survey.html')