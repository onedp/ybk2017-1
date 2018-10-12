"""ybk2017 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
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
from ybk.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('index', index),
    # path('test/aa', test1),
    path(r'box/<int:id>', test1,name='box'),
    path(r'surch', surch),
    path(r'ajaxtest1/', ajax2),
    path(r'bank/index/', bank_index),
    path(r'date1', date),
    path(r'sheet/<int:id>', sheet),
    path(r'inybk/', include('inybk.url')),

    # path(r,surch )




]


# 1:119 GET http://127.0.0.1:8000/test/static/plugins/picture/xue.jpg 404 (Not Found)