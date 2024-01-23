"""CodingIndiaERP URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from CodingIndiaERP.views import SignUpView, LoginView, LogoutView, VerifyOTP, VerifyLoginOTP

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('website.urls')),
    path('Project/', include('Project.urls')),
    path('Employee/', include('Employee.urls')),
    path('UserReq/', include('UserReq.urls')),
    

    #SignUp, Login
    path('Signup/', SignUpView, name="signup"),
    path('Login/', LoginView, name="login"),
    path('Logout/', LogoutView, name="logout"),

    path('verifyEmail/', VerifyOTP, name="verifyEmail"),
    path('verifyLogin/', VerifyLoginOTP, name="verifyLogin"),



] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
