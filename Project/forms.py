from django.forms import ModelForm
from Project.models import ProjectModel 

class ProjectForm(ModelForm):
    class Meta:
        model = ProjectModel
        # fields = ["name", "projectdate"]
        fields = '__all__'