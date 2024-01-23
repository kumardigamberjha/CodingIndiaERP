from django.shortcuts import render
from Project.models import ProjectModel
from Project.forms import ProjectForm

def CreateProject(request):
    form = ProjectForm()

    if request.method == "POST":
        form = ProjectForm(request.POST)

        if form.is_valid():
            form.save()        
            print("Form Saved")
        else:
            print("Form Error: ", form.errors)

    context = {'form': form}
    return render(request, 'Project/create_project.html', context)


def ShowprojectData(request):
    data = ProjectModel.objects.all()
    print("Data: ", data)
    
    context = {'data': data}
    return render(request, 'Project/showProjectData.html', context)