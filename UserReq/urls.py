from django.urls import path
from UserReq import views

urlpatterns = [
    path('', views.AddReq, name="add_req"),
    path('ShowReq', views.UserReqView, name="show_req"),
    path('UpdateReq/<int:id>/', views.UpdateReq, name="update_req"),
    path('DelReq/<int:id>/', views.DelReq, name="del_req"),
    
]