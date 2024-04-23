from django.shortcuts import get_object_or_404, redirect, render
from .models import Survey, Question, Option
from django.contrib.auth.decorators import login_required

# Create your views here.
#call survey template one

def index(request):
    return render(request, 'home1.html')



@login_required
def createsurvey(request):
    if request.method == 'POST':
        print(request.POST)
        title = request.POST['title']
        survey = Survey.objects.create(title=title, user=request.user)
        print(f"Survey title: {title}")  # Print survey title
        num_questions = sum(1 for key in request.POST if key.startswith('questions#_'))
        for i in range(1, num_questions + 1):
            question_text = request.POST['questions#_' + str(i)]
            question_type = request.POST['questionTypes_' + str(i)]
            question = Question.objects.create(text=question_text, type=question_type, survey=survey)
            print(f"Question {i}: {question_text} ({question_type})")  # Print question text and type
            if question_type != '(text)':
                print('it is working')
                prefix = 'questions_' + str(i) + '_options_'
                option_keys = [key for key in request.POST.keys() if key.startswith(prefix)]
                option_texts = [request.POST[key] for key in option_keys]
                print(option_texts)
                for option_text in option_texts:
                    Option.objects.create(text=option_text, question=question)
                    print(f"Option for question {i}: {option_text}")  # Print option text
        return redirect('preview_survey' , pk=survey.pk)

    return render(request, 'create_survey.html')
#Recreate edit_survey to take arguments Survey,Questions,Type, and options so that it can be called in the createsurvey function
#add proper responses to the function

def preview_survey(request, pk):
    survey = get_object_or_404(Survey, pk=pk)
    questions = survey.questions.all()
    print("Survey: ", survey.title)
    print("Questions: ")
    for question in questions:
        options = question.options.all()
        print("Question: ", question.text)
    context = {
        'survey': survey,
        'questions': questions,
    }
    return render(request, 'preview.html', context)


def survey_detail(request, pk):
    survey = get_object_or_404(Survey, pk=pk)
    questions = survey.questions.all()
    print("Survey: ", survey.title)
    for question in questions:
        print("Question: ", question.text)
        options = question.options.all()  # Retrieve options for the question
        for option in options:
            print("Option: ", option.text)
    context = {
        'survey': survey,
        'questions': questions,
    }
    return render(request, 'survey_detail.html', context)

def take_survey(request, pk):
    survey = get_object_or_404(Survey, pk=pk)
    questions = survey.questions.all()
    print("Survey: ", survey.title)
    print("Questions: ")
    for question in questions:
        options = question.options.all()
        print("Question: ", question.text)
    context = {
        'survey': survey,
        'questions': questions,
    }
    return render(request, 'take_survey.html', context)



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
