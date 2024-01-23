from django.forms import ModelForm
from Employee.models import Employee, Meeting

class EmployeeForm(ModelForm):
    class Meta:
        model = Employee
        fields = "__all__"


class MeetingForm(ModelForm):
    class Meta:
        model = Meeting
        fields = "__all__"