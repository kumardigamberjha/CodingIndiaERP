from django.shortcuts import render
from django.contrib.auth.models import User

def Index(request):
    return render(request, 'website/dashboard.html')


def ShowStaff(request):
    data = User.objects.all()

    context = {'data': data}
    return render(request, 'website/showStaff.html', context)



def ViewStaffData(request, id):
    data = User.objects.get(id=id)

    context = {'data': data}
    return render(request, 'website/viewstaffdata.html', context)