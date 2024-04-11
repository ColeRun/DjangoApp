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
                if i < len(options):
                    option_list = options[i].split(',')
                    for option_text in option_list:
                        Option.objects.create(text=option_text, question=question)
                else:
                    print(f"No options provided for question {i+1}")
        return createdsurvey(request, survey.pk)
    return render(request, 'create_survey.html')
#Recreate edit_survey to take arguments Survey,Questions,Type, and options so that it can be called in the createsurvey function
#add proper responses to the function


def survey_detail(request, pk):
    survey = get_object_or_404(Survey, pk=pk)
    questions = survey.question_set.all()
    for question in questions:
        print("Question: ", question.text)
        options = question.option_set.all()
        for option in options:
            print("Option: ", option.text)
    return render(request, 'survey_detail.html', {'survey': survey})
    
def take_survey(request, pk):
    survey = get_object_or_404(Survey, pk=pk)
    questions = survey.question_set.all()
    for question in questions:
        print("Question: ", question.text)
        options = question.option_set.all()
        for option in options:
            print("Option: ", option.text)
    return render(request, 'take_survey.html', {'survey': survey, 'questions': questions})
    
def user_surveys(request):
    surveys = Survey.objects.filter(user=request.user)
    return render(request, 'user_surveys.html', {'surveys': surveys})    

def all_surveys(request):
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
