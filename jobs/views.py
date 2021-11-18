from django.shortcuts import render

from .models import Job

def home(request):
    jobs = Job.objects
    return render(request, 'jobs/home.html', {'jobs':jobs})

def blog(request):
    blog = blog.objects
    return render(request, 'blog/allblogs.html')
