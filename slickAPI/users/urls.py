from django.urls import path 
from django.views import View

urlpatterns=[
    path("login/", View.as_view() ),
   
   
]