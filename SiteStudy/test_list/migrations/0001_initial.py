# Generated by Django 2.2.2 on 2019-10-17 18:14

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Test',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title_test', models.CharField(max_length=120)),
                ('text_test', models.TextField()),
                ('date_test', models.DateField()),
                ('img_test', models.CharField(max_length=120)),
                ('ID_person', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Quest_test',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title_quest_test', models.CharField(max_length=120)),
                ('text_quest_test', models.TextField()),
                ('true_answer', models.CharField(max_length=120)),
                ('img_quest_test', models.CharField(max_length=120)),
                ('ID_test', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='test_list.Test')),
            ],
        ),
    ]
