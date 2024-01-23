from django.urls import path
from Employee import views

urlpatterns =[
    path('', views.AddEmployee, name= "addEmployee"),
    path('AddMeeting/', views.AddMeeting, name="addmeeting")
]