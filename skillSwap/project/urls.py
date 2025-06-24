from django.urls import path
from . import views

urlpatterns = [
    path('add-project/',views.addProject, name='addProject'),
    path('view-project/',views.viewProject, name='viewProject'),
    path('edit-project/',views.editProject, name='editProject'),
    path('detail-project/',views.detailProject,name='detailProject'),
    
]