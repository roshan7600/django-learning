"""
URL configuration for college project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
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
from django.urls import path,include
import BE,BTECH,MCA

urlpatterns = [
    path('admin/', admin.site.urls),
    path('MCA/' ,include('MCA.urls')),
    path('BE/' , include('BE.urls')),
    path('BTECH/', include('BTECH.urls')),
    path('BBA/' ,include('BBA.urls')),
    path('BSC/' , include('BSC.urls')),
    path('BARCH/', include('BARCH.urls')),

    path('MSC/' ,include('MSC.urls')),
    path('MBA/' , include('MBA.urls')),
    



]
