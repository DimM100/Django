# Generated by Django 2.2.2 on 2019-10-07 17:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_list', '0004_news_img_1_news'),
    ]

    operations = [
        migrations.CreateModel(
            name='Kims',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title_kim', models.CharField(max_length=120)),
                ('text_kim', models.TextField()),
                ('adress_kim', models.CharField(max_length=120)),
            ],
        ),
    ]