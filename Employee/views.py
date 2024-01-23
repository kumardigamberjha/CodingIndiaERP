from django.shortcuts import render
from Employee.models import Employee, Meeting
from Employee.forms import EmployeeForm, MeetingForm
from CodingIndiaERP.forms import CreateUserForm

def AddEmployee(request):
    form = EmployeeForm()
    form2 = CreateUserForm()
    if request.method == "POST":
        form = EmployeeForm(request.POST)
        form2 = CreateUserForm(request.POST)

        if form.is_valid() and form2.is_valid():
            form.save()
            form2.save()

            print("Form Saved")
        else:
            print("Form Error: ", form.errors)
            print("Form2 Error: ", form2.errors)

    context = {'form': form, }
    return render(request, 'Employee/addEmployee.html', context)


def AddMeeting(request):
    member = Employee.objects.all()
    form = MeetingForm()
    if request.method == "POST":
        form = MeetingForm(request.POST)

        if form.is_valid():
            form.save()
            print("Form Saved")
        else:
            print("Form Error: ", form.errors)
    context = {'member': member}
    return render(request, 'Employee/addmeeting.html', context)


def ShowMeeting(request):
    meeting = Meeting.objects.filter()
    context = {}
    return render(request, 'Employee/show_meetings.html', context)