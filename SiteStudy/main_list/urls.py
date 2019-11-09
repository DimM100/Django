from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name = 'index'),
    path('quest', views.quest_index, name = 'quest_index'),
    path('resume', views.resume_index, name = 'resume_index'),
    path('theory', views.theory_index, name = 'theory_index'),
    path('kim', views.kim_index, name = 'kims')
]
