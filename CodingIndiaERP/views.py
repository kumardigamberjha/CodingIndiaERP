from django.shortcuts import render, redirect

from CodingIndiaERP.forms import CreateUserForm
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.core.mail import send_mail
from CodingIndiaERP.settings import EMAIL_HOST_USER
import random
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.models import User


@csrf_exempt
def VerifyOTP(request):
    if request.method == "POST":
        userotp = request.POST.get('otp')
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        username = request.POST.get('username')
        email = request.POST.get('email')
        password1 = request.POST.get('password1')
        password2 = request.POST.get('password2')

        if password1 == password2:
            form = User(first_name=first_name, last_name=last_name, email=email, username=username, password = password1)
            form.save()

        print("OTP: ", userotp)
    return JsonResponse({'data': 'Hello'}, status=200)


def SignUpView(request):
    form = CreateUserForm()
    if request.method == "POST":
        email = request.POST.get('email')
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        username = request.POST.get('username')
        password1 = request.POST.get('password1')
        password2 = request.POST.get('password2')

        form = CreateUserForm(request.POST)

        if form.is_valid():
            
            # form.save()
            otp = random.randint(100000, 999999)
            send_mail("User Data: ", f"Verify Your Mail by the OPT: /n {otp}", EMAIL_HOST_USER, [email], fail_silently=True)
            messages.success(request, 'User saved Successfully')
            return  render(request, 'website/verify.html', {'otp': otp, 'first_name': first_name, 'last_name': last_name, 'email': email, 'username': username, 'password1': password1, 'password2': password2})
            
        else:
            print("Form Error: ", form.errors)
            messages.error(request, form.errors)
    context = {'form': form}
    return render(request, 'website/signup.html', context)



@csrf_exempt
def VerifyLoginOTP(request):
    if request.method == "POST":
        userotp = request.POST.get('otp')
        username = request.POST.get('username')
        # email = request.POST.get('email')
        password = request.POST.get('password')
        
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            print("Login Done")

        print("OTP: ", userotp)
    return JsonResponse({'data': 'Hello'}, status=200)


def LoginView(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        email = User.objects.get(username=username).email
        print("Username: ", username)
        print("password: ", password)
        print("Email: ", email)


        user = authenticate(request, username=username, password=password)
        if user is not None:
            otp = random.randint(100000, 999999)
            send_mail("User Data: ", f"Verify Your Mail by the OPT: /n {otp}", EMAIL_HOST_USER, [email], fail_silently=True)
            messages.success(request, 'User saved Successfully')
            return  render(request, 'website/verifyLogin.html', {'otp': otp, 'username': username, 'password': password})

        else:
            messages.error(request, 'Invalid Entry')

    context = {}
    return render(request, 'website/login.html', context)


def LogoutView(request):
    logout(request)
    print("Logout Successfull")
    messages.success(request, 'Logout Successful')

    return redirect('login')