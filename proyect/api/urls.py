from django.urls import path 
from . import views

urlpatterns=[  # Fixed the typo: was "urlspattners"
    path('code', views.main)
]