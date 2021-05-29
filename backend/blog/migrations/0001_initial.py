# Generated by Django 3.1.4 on 2021-05-29 15:16

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='BlogPost',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('slug', models.SlugField()),
                ('category', models.CharField(choices=[('Web Development', 'Webdevelopment'), ('python', 'Python'), ('technology', 'Technology'), ('Web design', 'Webdesign'), ('programming', 'Programming'), ('data visualization', 'Datavisualization'), ('opinion', 'Opinion'), ('fundamentals', 'Fundamentals'), ('productivity', 'Productivity')], default='programming', max_length=50)),
                ('thumbnail', models.ImageField(upload_to='photos/%Y/%m/%d/')),
                ('excerpt', models.CharField(max_length=250)),
                ('month', models.CharField(max_length=3)),
                ('day', models.CharField(max_length=2)),
                ('content', models.TextField()),
                ('featured', models.BooleanField(default=False)),
                ('date_created', models.DateTimeField(blank=True, default=datetime.datetime.now)),
            ],
        ),
    ]
