from django.shortcuts import render
from django.http import HttpResponse

import os

def index(request):
    return render(request, 'home/index.html')

def resume(request):
    # with open('project_static/mark_mcdonald_resume.pdf', 'rb') as pdf:
    #     response = HttpResponse(pdf.read(), content_type='application/pdf')
    #     response['Content-Disposition'] = 'filename=mark_mcdonald_resume.pdf'
    #     return response
    # pdf.closed
    return render(request, 'home/resume.html')
