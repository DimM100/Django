from django.shortcuts import render
from .models import News, Quest, User_p, Skills, Study_place, Theory, Kims
from django.contrib.auth.models import User
from regauth.views import check_autorization

@check_autorization
def index(request):
    news = News.objects.order_by("-id")
    context = {"news": news, "user": request.user.username}

    return render(request, 'main_list/index.html', context)

@check_autorization
def quest_index(request):
    quest = Quest.objects.order_by("id")
    context = {"questions": quest, "user": request.user.username}

    return render(request, 'main_list/quest_index.html', context)

@check_autorization
def resume_index(request):
    user = User.objects.get(id = 1)
    user_p = User_p.objects.get(ID_person = user)
    study_places = Study_place.objects.filter(ID_person = user)
    skills = Skills.objects.filter(ID_person = user)

    context = {"user_c": user, "user_p": user_p, "study_places": study_places, "skills": skills, "user": request.user.username}

    return render(request, 'main_list/resume_index.html', context)

@check_autorization
def theory_index(request):
    theory = Theory.objects.order_by("id")
    context = {"theories": theory, "user": request.user.username}
    return render(request, 'main_list/theory_index.html', context)

@check_autorization
def kim_index(request):
    kims = Kims.objects.order_by("id")
    context = {"kims": kims, "user": request.user.username}
    return render(request, 'main_list/kim_index.html', context)
# Create your views here.
