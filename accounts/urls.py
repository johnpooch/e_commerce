from django.urls import path
from accounts.views import login, register, logout, profile
from django.contrib.auth.views import password_reset, password_reset_done, password_reset_confirm, password_reset_complete

urlpatterns = [
    path('login', login, name="login"),
    path('register', register, name="register"),
    path('logout', logout, name="logout"),
    path('profile', profile, name="profile"),
]