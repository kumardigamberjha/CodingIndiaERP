from django.shortcuts import render, redirect
from UserReq.forms import ReqForm
from UserReq.models import Requisition

def AddReq(request):
    form = ReqForm()

    if request.method == "POST":
        form = ReqForm(request.POST)

        print(request.POST)

        if form.is_valid():
            form.save()
            print("Form Saved")
        else:
            print("Form Error: ", form.errors)
    context = {}
    return render(request, 'UserReq/add_req.html', context)



def UserReqView(request): 
    data = Requisition.objects.all()
    context = {'data': data}
    return render(request, 'UserReq/show_req.html', context)


def UpdateReq(request, id):
    data = Requisition.objects.get(id = id)
    form = ReqForm(instance=data)

    if request.method == "POST":
        form = ReqForm(request.POST, instance=data)

        print(request.POST)

        if form.is_valid():
            form.save()
            print("Form Saved")
        else:
            print("Form Error: ", form.errors)
    context = {'data': data}
    return render(request, 'UserReq/add_req.html', context)


def DelReq(request, id):
    data = Requisition.objects.get(id=id)
    data.delete()
    print("Deleted")
    return redirect('show_req')