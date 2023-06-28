from django.urls import path
from . import views

urlpatterns=[
    path('',views.Index ),
    path('login/', views.loginview, name='login'),
    path('profiledata/', views.ProfileData, name='profiledata')
]