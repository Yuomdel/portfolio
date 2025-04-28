from django.shortcuts import render
from projects.models import Skill, Project
from pages.forms import ContactForm
from django.core.mail import send_mail
from django.conf import settings

def home(request):
    skills = Skill.objects.all()
    featured_projects = Project.objects.all()[:3]
    context = {
        'skills': skills,
        'projects': featured_projects
    }
    return render(request, 'pages/home.html', context)

def projects(request):
    all_projects = Project.objects.all()
    context = {
        'projects': all_projects
    }
    return render(request, 'projects/projects.html', context)

def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            # Save to database
            message = form.save()
            
            # Send email
            # send_mail(
            #     f"New message from {message.name}",
            #     message.message,
            #     message.email,
            #     [settings.DEFAULT_FROM_EMAIL],
            #     fail_silently=False,
            # )
            
            return render(request, 'pages/contact.html', {'success': True},)
    else:
        form = ContactForm()
    
    return render(request, 'pages/contact.html', {'form': form})
