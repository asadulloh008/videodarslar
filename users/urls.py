from django.contrib import admin
from django.urls import path,include
from .views import signup,login,sign_or_log

app_name="users"

urlpatterns = [
    path('', sign_or_log, name="sign_or_log"),
    path('signup/', signup, name='signup'),
    path('login/', login, name='login'),
]