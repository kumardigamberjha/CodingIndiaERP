from django.urls import path
# from . import views
from Project import views

urlpatterns = [
    path('', views.CreateProject, name="create_project"),
    path('ShowProjectData/', views.ShowprojectData, name="show_project_data"),

]