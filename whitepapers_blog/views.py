from whitepapers_blog.models import UserProfileInfo, WhitePapers
from whitepapers_blog.forms import UserForm
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from whitepapers_blog.forms import UserForm, UserProfileInfoForm
from rest_framework import viewsets
from whitepapers_blog.serializers import WhitePapersSerializer
from rest_framework.schemas import AutoSchema
from rest_framework.response import Response
from rest_framework.views import APIView
from requests import Request, Session
from requests.exceptions import ConnectionError, Timeout, TooManyRedirects
import json
import coreapi
import requests


class WhitePapersViewSet(viewsets.ModelViewSet):
    queryset = WhitePapers.objects.all()
    serializer_class = WhitePapersSerializer


#login
from django.urls import reverse 
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout


# Create your views here.
def get_prices(request):
    url = 'https://pro-api.coinmarketcap.com/v1/cryptocurrency/listings/latest'
    parameters = {
    'start':'1',
    'limit':'10',
    'convert':'USD'
    }
    headers = {
    'Accepts': 'application/json',
    'X-CMC_PRO_API_KEY': '87248676-d165-417d-975a-75f107781bce',
    }

    session = Session()
    session.headers.update(headers)

    response = session.get(url, params=parameters)
    data = json.loads(response.text)
    return render(request, "whitepapers_blog/trading.html", {"data": data})

def Vectorspace_Summerizer(request):

    url = "https://vectorspaceai-vectorspace-ai-summarizer-v1.p.rapidapi.com/recommend/app/summarize"

    querystring = {"query":"text","vxv_token_addr":"0xC2A568489BF6AAC5907fa69f8FD4A9c04323081D"}

    headers = {
        'x-rapidapi-key': "8200c4be52msh500d32be82b9abcp16c7b0jsn847107d6e2f7",
        'x-rapidapi-host': "vectorspaceai-vectorspace-ai-summarizer-v1.p.rapidapi.com"
        }
    response = requests.request("GET", url, headers=headers, params=querystring)
    data = json.loads(response.text)
    print(response.text)
    print(data)
    return render(request, "whitepapers_blod/test.html", {"data": data})
    
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


class CustomLoginSchema(AutoSchema):

    def get_serializer_fields(self, path, method):
        if method == 'POST':
            extra_fields = [
                coreapi.Field('username',
                              required=True,
                              location="formData",
                              type="string"
                              ),
                coreapi.Field('password',
                              required=True,
                              location="formData",
                              type="string"
                              ),
            ]
        else:
            extra_fields = []
        serializer_fields = super().get_serializer_fields(path, method)
        return serializer_fields + extra_fields

class AuthUserAPIView(APIView):
    def post(self, request, *args, **kwargs):#in this function, define custom logic
        pass