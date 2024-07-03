from django.shortcuts import render
from .models import PersonalInfo, Education, Skill, Experience, Project, Contact

def home(request):
    personal_info = PersonalInfo.objects.first()
    education = Education.objects.all()
    skills = Skill.objects.all()
    experiences = Experience.objects.all()
    projects = Project.objects.all()
    contact = Contact.objects.all()
    return render(request, 'home.html', {
        'personal_info': personal_info,
        'education': education,
        'skills': skills,
        'experiences': experiences,
        'projects': projects,
        'contact': contact
    })
def contact(request):
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        message = request.POST['message']
        contact = Contact(name=name, email=email, message=message)
        contact.save()
        return render(request, 'thanks.html')
    return render(request, 'contact.html')
