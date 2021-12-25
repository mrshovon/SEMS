from django.urls import path
from . import views


urlpatterns = [
    path('',views.loginPage,name="loginPage"),
    path('logoutUser',views.logoutUser,name="logoutUser"),
    path('studentHome',views.studentHome,name="studentHome"),
    path('admissionForm',views.admissionForm,name="admissionForm"),
    
    
]