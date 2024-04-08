from django.shortcuts import get_object_or_404, render
from .models import Survey, Question, Option
from django.contrib.auth.decorators import login_required

# Create your views here.
#call survey template one

def index(request):
    return render(request, 'home1.html')

@login_required
def createsurvey(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        questions = request.POST.getlist('questions')
        question_types = request.POST.getlist('questionTypes')
        options = request.POST.getlist('options')
        survey = Survey(title=request.POST['title'], user=request.user)
        survey.save()
        print("survey created")
       
        for i in range(len(questions)):
            question = Question.objects.create(text=questions[i], type=question_types[i], survey=survey)
            if question_types[i] != 'text':
                for j in range(len(options)):
                    Option.objects.create(text=options[j], question=question)
        return createdsurvey(request, survey.pk)
    return render(request, 'create_survey.html')


def survey_detail(request, pk):
    survey = get_object_or_404(Survey, pk=pk)
    return render(request, 'survey_detail.html', {'survey': survey})
    

    
def user_surveys(request):
    surveys = Survey.objects.all()
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
    surveys = Survey.objects.filter(user=request.user)
    return render(request, 'created_surveys.html', {'surveys': surveys})
