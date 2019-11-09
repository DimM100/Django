from django.db import models
from django.contrib.auth.models import User

class Test(models.Model):
    title_test = models.CharField(max_length = 120)
    text_test = models.TextField()
    date_test = models.DateField()
    img_test = models.CharField(max_length = 120)
    ID_person = models.ForeignKey(User, on_delete = models.PROTECT)

    def __str__(self):
        return str(self.id) + ": " + self.title_test

class Quest_test(models.Model):
    title_quest_test = models.CharField(max_length = 120)
    text_quest_test = models.TextField()
    true_answer = models.CharField(max_length = 120)
    img_quest_test = models.CharField(max_length = 120)
    ID_test = models.ForeignKey(Test, on_delete = models.PROTECT)

    def __str__(self):
        return str(self.id) + ": " + self.title_quest_test

class Result_test(models.Model):
    count_right_answer = models.CharField(max_length = 120)
    ID_person = models.ForeignKey(User, on_delete = models.PROTECT)
    ID_test = models.ForeignKey(Test, on_delete = models.PROTECT)
# Create your models here.
