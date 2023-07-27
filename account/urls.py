from django.contrib import admin
from django.urls import path,include
from account.views import UserRegistration,UserLoginView,UserProfile
urlpatterns = [
    path('register/',UserRegistration.as_view(),name='register'),
    path('login/',UserLoginView.as_view(),name='login'),
    path('profile/',UserProfile.as_view(),name='profile')
]
