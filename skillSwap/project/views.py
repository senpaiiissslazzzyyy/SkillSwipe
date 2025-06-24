from django.shortcuts import get_object_or_404, render, redirect
from accounts.models import UserProfile
from accounts.forms import UserForm, UserProfileForm
from .forms import ProjectForm
from project.models import Project

# Create your views here.

def viewProject(request):
    return render(request,'project/viewProject.html')

def editProject(request):
    return render(request,'project/editProject.html')

def detailProject(request):
    return render(request,'project/detailProject.html')

def addProject(request):
    if request.method == 'POST':
        form = ProjectForm(request.POST)
        if form.is_valid():
            project = form.save(commit=False)
            project.user = request.user
            project.save()
            return redirect('viewProject')  
    else:
        form = ProjectForm()
        
    context={
        'form':form
    }
    return render(request, 'project/addProject.html', context)

# def project_list(request):
#     projects = Project.objects.filter(user=request.user)
#     context={'projects': projects}
#     return render(request, 'viewProject.html', context)
