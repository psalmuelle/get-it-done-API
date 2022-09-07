from django.urls import path
from knox import views as knox_views
from . import views

urlpatterns = [
    path('user/', views.get_user),
    path('login/', views.login),
    path('register/', views.register),
    path(r'logout/', views.logout),
    path(r'logoutall/', knox_views.LogoutAllView.as_view(), name='knox_logoutall'),
]