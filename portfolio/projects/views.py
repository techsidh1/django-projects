from django.shortcuts import render, get_object_or_404
from .models import Project, Person, Blog 

def home(request):
    projects = Project.objects.all()
    person = Person.objects.all()
    
    context = {
        'projects': projects,
        'person': person
        }

    return render(request, 'projects/home.html', context)


def mynotes(request):
    tag = request.GET.get('tag')
    if tag:
        notes = Blog.objects.filter(tags__name__in=[tag])
        return render(request, 'projects/mynotes.html', {'notes': notes})
    else:
        notes = Blog.objects.all().order_by('-created_at')
        return render(request, 'projects/mynotes.html', {'notes': notes})

def mynotedetails(request, slug):
    note = Blog.objects.get(slug=slug)
    return render(request, 'projects/mynotedetails.html', {'note':note})
