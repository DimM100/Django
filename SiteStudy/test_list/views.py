from django.shortcuts import render, redirect
from .models import Test, Quest_test, Result_test
from django.contrib.auth.models import User
from regauth.views import check_autorization

@check_autorization
def test_index(request):
    if request.session['ID_test']:
        if(request.method == 'POST'):
            result = Result_test()
            result.count_right_answer = request.POST.get("button")
            result.ID_person = request.user
            result.ID_test = Test.objects.get(pk = request.session['ID_test'])
            del request.session['ID_test']
            result.save()
            return redirect('/test')

        test = Test.objects.get(pk = request.session['ID_test'])
        quests = Quest_test.objects.filter(ID_test = test)
        context = {"test": test, "quests": quests, "user": request.user.username}

        return render(request, 'test_list/index.html', context)
    else:
        return redirect('/test')

@check_autorization
def test_lobby_index(request):
    tests = Test.objects.order_by("-id")
    context = {"tests": tests}

    if(request.method == 'POST'):
        request.session['ID_test'] = request.POST.get("radio-test-chose")
        return redirect('/test/test_begin')

    return render(request, 'test_list/index_lobby.html', context)
# Create your views here.
