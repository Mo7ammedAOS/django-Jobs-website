from django.urls import reverse
from multiprocessing import context
import re
from django.shortcuts import render , redirect
from .forms import SignupForm , UserForm , ProfileForm
from django.contrib.auth import authenticate , login
from .models import Porofile

# Create your views here. 
def signup(request):
    if request.method =='POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data('username')
            password = form.changed_data('password1')
            user = authenticate(username=username,password=password)
            login(request,user)
            redirect('/accounts/profile ')
    else:
        form =SignupForm()

    context ={'form':form}
    return render(request,'registration/signup_form.html',context)



def profile(request):
    profile = Porofile.objects.get(user = request.user)
    context ={'profile':profile}
    return render(request,'accounts/profile.html',context)

def edit_profile(request):
    profile = Porofile.objects.get(user=request.user)

    if request.method == 'POST':
        usform = UserForm(request.POST,instance=request.user)
        prform = ProfileForm(request.POST,request.FILES,instance=profile)
        if usform.is_valid() and prform.is_valid():
            usform.save()
            prform.save(commit=False)
            prform.user = request.POST
            prform.save()
            return redirect(reverse('accounts:profile'))
    else:
        usform = UserForm(instance=request.user)
        prform = ProfileForm(instance=profile)

    context={'usform':usform,'prform':prform}
    return render(request,'accounts/profile_edit.html',context)