from django.shortcuts import render
from .models import Job, Skill, Education
from django.http import HttpResponse


def index(request):
    # return HttpResponse("This is the jobs homepage")
    jobs = Job.objects
    skills = Skill.objects
    education = Education.objects
    return render(request, 'work_history/index.html', {'jobs': jobs, 'skills': skills, 'education': education})
