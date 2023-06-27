# Generated by Django 4.2 on 2023-06-27 21:19

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('freelancer', '0002_project_tags'),
    ]

    operations = [
        migrations.AddField(
            model_name='employer',
            name='description',
            field=models.TextField(default='No Description Provided'),
        ),
        migrations.AddField(
            model_name='project',
            name='created_at',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.RemoveField(
            model_name='project',
            name='tags',
        ),
        migrations.AddField(
            model_name='project',
            name='tags',
            field=models.ManyToManyField(to='freelancer.skill'),
        ),
    ]
