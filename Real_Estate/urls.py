"""
URL configuration for Project_Name project.

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
from admins import views as AdminViews
from users import views as UserViews


urlpatterns = [
    path('admin/', admin.site.urls),

    path('', AdminViews.AdminBasePage, name='base' ),
    path('home', AdminViews.home, name='home' ),

   
   
    path('prediction_view', UserViews.prediction_view, name='prediction_view' ),  
    path('userhome', UserViews.userhome, name='userhome' ),
    path('userAddedValues',UserViews.userAddedValues,name='userAddedValues'),
    path('model_values', UserViews.model_values, name='model_values' ),  

    path('adminhome', AdminViews.adminhome, name='adminhome' ),
    path('userlogin', AdminViews.UserLoginPage, name='userlogin'),
    path('adminlogin', AdminViews.AdminLoginPage, name='adminlogin'),
    path('register/', AdminViews.UserRegisterPage, name='register'),
    path('userlist', AdminViews.UsersViewPage, name='userlist'),
    path('userActivate/', AdminViews.ActivateUser, name='userActivate'),
    path('userDeactivate/', AdminViews.DeactivateUser, name='userDeactivate'),
    path('userAddedValuesApprovel',AdminViews.userAddedValuesApprovel,name='userAddedValuesApprovel'),
    path('approve_property',AdminViews.approve_property,name='approve_property'),
    path('delete_property',AdminViews.delete_property,name='delete_property'),
    
    
    
]
