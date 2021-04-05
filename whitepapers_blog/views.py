from whitepapers_blog.models import UserProfileInfo
from whitepapers_blog.forms import UserForm
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from whitepapers_blog.forms import UserForm, UserProfileInfoForm
from rest_framework import viewsets
from whitepapers_blog.models import WhitePapers
from whitepapers_blog.serializers import WhitePapersSerializer


class WhitePapersViewSet(viewsets.ModelViewSet):
    queryset = WhitePapers.objects.all()
    serializer_class = WhitePapersSerializer


#login
from django.urls import reverse 
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout


# Create your views here.
def index(request):
    return render(request, 'whitepapers_blog/index.html')

def register(request):  

    registered = False
    if request.method == "POST":
        user_form = UserForm(data=request.POST)
        profile_form = UserProfileInfoForm(data=request.POST)

        if user_form.is_valid() and profile_form.is_valid():

            user = user_form.save()
            user.set_password(user.password)
            user.save()

            profile = profile_form.save(commit=False)
            profile.user = user

            if 'profile_pic' in request.FILES:
                profile.profile_pic = request.FILES['profile_pic']

            profile.save()

            registered = True
        else:
            print(user_form.errors, profile_form.errors)
    else:
        user_form = UserForm()
        profile_form = UserProfileInfoForm()

    return render(request, 'whitepapers_blog/registration.html', {'user_form':user_form, 'profile_form':profile_form, 'registered':registered})