from django.shortcuts import render, redirect, get_object_or_404
from .models import Question, Answer
from .forms import RegisterForm, QuestionForm, AnswerForm
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required

def home(request):
    questions = Question.objects.all().order_by('-created_at')
    return render(request, 'core/home.html', {'questions': questions})

def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home')
    else:
        form = RegisterForm()
    return render(request, 'core/register.html', {'form': form})

@login_required
def ask_question(request):
    if request.method == 'POST':
        form = QuestionForm(request.POST)
        if form.is_valid():
            question = form.save(commit=False)
            question.user = request.user
            question.save()
            return redirect('home')
    else:
        form = QuestionForm()
    return render(request, 'core/ask_question.html', {'form': form})

def view_question(request, pk):
    question = get_object_or_404(Question, pk=pk)
    answers = question.answers.all()
    form = AnswerForm()
    return render(request, 'core/view_question.html', {'question': question, 'answers': answers, 'form': form})

@login_required
def answer_question(request, pk):
    question = get_object_or_404(Question, pk=pk)
    if request.method == 'POST':
        form = AnswerForm(request.POST)
        if form.is_valid():
            answer = form.save(commit=False)
            answer.user = request.user
            answer.question = question
            answer.save()
    return redirect('view_question', pk=pk)

@login_required
def like_answer(request, pk):
    answer = get_object_or_404(Answer, pk=pk)
    answer.likes.add(request.user)
    return redirect('view_question', pk=answer.question.pk)

@login_required
def logout_view(request):
    logout(request)
    return redirect('home')

