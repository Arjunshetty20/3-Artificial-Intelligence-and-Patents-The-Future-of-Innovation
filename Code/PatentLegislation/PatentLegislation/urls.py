"""PatentLegislation URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from django.conf import settings
from django.conf.urls.static import static
from users import views as users
from admins import views as admins
from copyright import views as copyright

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', users.index, name='index'),
    path('index/', users.index, name='index'),
    path('logout/', users.logout, name='logout'),
    path('userlogin/', users.userlogin, name='userlogin'),
    path('userregister/', users.userregister, name='userregister'),
    path('userlogincheck/', users.userlogincheck, name='userlogincheck'),
    path('upload/', users.upload, name='upload'),
    path('granted/', users.granted, name='granted'),

    path('adminlogin/', admins.adminlogin, name='adminlogin'),
    path('adminloginentered/', admins.adminloginentered, name='adminloginentered'),
    path('viewusers/', admins.viewusers, name='viewusers'),
    path('activateuser/', admins.activateuser, name='activateuser'),
    path('viewdata/', admins.viewdata, name='viewdata'),
    path('AdminAccept/', admins.AdminAccept, name='AdminAccept'),
    path('AdminDelete/', admins.AdminDelete, name='AdminDelete'),


    path('copyrightadministered/', copyright.copyrightadministered, name='copyrightadministered'),
    path('copyrightloginentered/', copyright.copyrightloginentered, name='copyrightloginentered'),
    path('permissions/', copyright.permissions, name='permissions'),
    path('sendpermission/', copyright.sendpermission, name='sendpermission'),
    path('sendreject/', copyright.sendreject, name='sendreject'),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)