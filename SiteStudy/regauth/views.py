from django.shortcuts import render, redirect

from django.views.generic.edit import FormView
from django.contrib.auth.forms import UserCreationForm

class RegisterFormView(FormView):
    form_class = UserCreationForm
    success_url = "/login"
    template_name = "regauth/register.html"

    def form_valid(self, form):
        form.save()
        return super(RegisterFormView, self).form_valid(form)

from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login

class LoginFormView(FormView):
    form_class = AuthenticationForm
    success_url = "/"
    template_name = "regauth/login.html"


    def form_valid(self, form):
        self.user = form.get_user()
        login(self.request, self.user)
        return super(LoginFormView, self).form_valid(form)

def check_autorization(index):
    def check_autor(request):
        if(request.user.is_authenticated):
            return index(request) # Сама функция
        else:
            return redirect('/login')
    return check_autor
