"""adminka URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from cmath import log
from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from users.views import login_view, register_view, profile_view, logout_view
from mainapp.views import main_view

urlpatterns = [
    path('', main_view),
    path('admin/', admin.site.urls),
    path('login/', login_view, name='login_view'),
    path('register/', register_view, name='register_view'),
    path('profile/', profile_view, name='profile_view'),
    path('logout/', logout_view, name='logout_view')
    
]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
