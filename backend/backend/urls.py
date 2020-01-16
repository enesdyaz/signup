"""backend URL Configuration

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
from django.urls import path, include
from rest_framework_jwt.views import obtain_jwt_token, refresh_jwt_token, verify_jwt_token


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('core.urls')),

    #rest_framework_jwt_views
    path('api-token-auth/', obtain_jwt_token),
    path('api-token-refresh/', refresh_jwt_token),
    path('api-token-verity/', verify_jwt_token),

    #SIGNUP, LOGIN, LOGOUT endpoint
    path('rest-auth/', include('rest_auth.urls')), #LOGIN(username or email, password), LOGOUT(token will be deleted)
    path('rest-auth/registration/', include('rest_auth.registration.urls')),  #SIGNUP (username, email, password1, password2)

]
