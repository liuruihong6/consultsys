"""
URL configuration for consultsys project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from django.urls import path
from 保单跟进.views import datas
from 咨询.views import datas1
from 产品管理.views import details,details2,details3,details4,details5,details6
urlpatterns = [
    path('admin/', admin.site.urls),
    path('update_data/', datas),
    path('update/', datas1),
    path('details/', details),
    path('details2/', details2),
    path('details3/', details3),
    path('details4/', details4),
    path('details5/', details5),
    path('details6/', details6),
]



