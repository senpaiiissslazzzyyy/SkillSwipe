from django.shortcuts import render

# Create your views here.

def viewProject(request):
    return render(request,'project/viewProject.html')

def editProject(request):
    return render(request,'project/editProject.html')

def detailProject(request):
    return render(request,'project/detailProject.html')
