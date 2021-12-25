from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth import authenticate, login, logout

from django.contrib import messages
from django.contrib.auth.decorators import login_required

def loginPage(request):
    if request.method =="POST":
        username= request.POST.get('username')
        password= request.POST.get('password')

        user=authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('studentHome')
        else:
            messages.info(request,('Username or password incorrect...!!!'))
            return render(request, 'loginPage.html', {})

    
    return render(request, 'loginPage.html', {})


def logoutUser(request):
    logout(request)
    return redirect('loginPage')


@login_required(login_url='loginPage')
def studentHome(request):                       
    return render(request, 'studentHome.html')

def admissionForm(request):
    return render(request,'admissionForm.html')
