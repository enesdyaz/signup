from django.urls import path, include
from . import views

urlpatterns = [
    path('user/', views.CustomUserView.as_view()),
]
