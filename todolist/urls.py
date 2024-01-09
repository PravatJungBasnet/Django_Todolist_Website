"""
URL configuration for todolist project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from task import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.home,name='hm'),
    path('det/<int:id>/',views.detail, name='det'),
    path('up/<int:id>/',views.update, name='up'),
    path('del/<int:id>/',views.delete,name='del'),
    path('sig/',views.signup,name='sig'),
    path('log/',views.user_login,name='log'),
    path('out/',views.user_logout,name='out'),
    path('add/',views.Add_task,name='add'),
    path('set/',views.change_pass,name='set')

  
]
