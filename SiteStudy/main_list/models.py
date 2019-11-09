from django.db import models
from django.contrib.auth.models import User

class News(models.Model):
    title_news = models.CharField(max_length = 120)
    text_news = models.TextField()
    date_news = models.DateField()
    img_news = models.CharField(max_length = 120)
    ID_person = models.ForeignKey(User, on_delete=models.PROTECT)

    def __str__(self):
        return str(self.id) + ": " + self.title_news

class Theory(models.Model):
    title_theory = models.CharField(max_length = 120)
    text_theory = models.TextField()
    date_theory = models.DateField()
    ID_person = models.ForeignKey(User, on_delete=models.PROTECT)

    def __str__(self):
        return str(self.id) + ": " + self.title_theory

class Quest(models.Model):
    title_quest = models.CharField(max_length = 120)
    text_quest = models.TextField()
    text_response_quest = models.TextField()
    date_quest = models.DateField()
    img_quest = models.CharField(max_length = 120)
    ID_person = models.ForeignKey(User, on_delete=models.PROTECT)

    def __str__(self):
        return str(self.id) + ": " + self.title_quest

class Study_place(models.Model):
    name_spl = models.CharField(max_length = 120)
    name_facult_spl = models.CharField(max_length = 120)
    name_way_spl = models.CharField(max_length = 120)
    date_start_stady = models.DateField()
    date_finish_stady = models.DateField()
    ID_person = models.ForeignKey(User, on_delete=models.PROTECT)

    def __str__(self):
        return str(self.id) + ": " + self.name_spl + " - " + self.name_way_spl

class Skills(models.Model):
    title_skill = models.CharField(max_length = 120)
    text_skill = models.TextField()
    ID_person = models.ForeignKey(User, on_delete=models.PROTECT)

    def __str__(self):
        return str(self.id) + ": " + self.title_skill

class User_p(models.Model):
    birthday = models.DateField()
    text_user = models.TextField()
    image_adress = models.CharField(max_length = 120, blank=True)
    ID_person = models.ForeignKey(User, on_delete=models.PROTECT)

    def __str__(self):
        return str(self.ID_person)

class Kims(models.Model):
    title_kim = models.CharField(max_length = 120)
    text_kim = models.TextField()
    adress_kim = models.CharField(max_length = 120)

    def __str__(self):
        return str(self.id) + ": " + self.title_kim
# Create your models here.
