"""project_crypto URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from django.conf.urls import url
from whitepapers_blog import views
from rest_framework import routers
from rest_framework_swagger.views import get_swagger_view
from django.conf.urls import url, include
from whitepapers_blog.views import AuthUserAPIView, get_prices, Vectorspace_Summerizer

schema_view = get_swagger_view(title='whitepapers_blog')
router = routers.DefaultRouter()
router.register(r'WhitePapers', views.WhitePapersViewSet)

urlpatterns = [
    path('asd', include('whitepapers_blog.urls')),
    path('admin/', admin.site.urls),
    # path('coinrank/', include('coinrank.urls')),
    url(r'^$', views.index, name='index'),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    url(r'^', include(router.urls)),
    url(r'^api/docs/', schema_view, name='api-doc'),
    url(r'^user/auth/login?$', AuthUserAPIView.as_view(), name='login_user'),
    url(r'^trade/', views.get_prices, name='trade'),
    url(r'^test/', views.Vectorspace_Summerizer, name='test'),
    # url(r'^whitepapers_blog/', include('whitepapers_blog.urls')),
]
