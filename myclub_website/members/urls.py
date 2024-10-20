from django.urls import path
from . import views

urlpatterns = [
  path('login-user', views.login_user, name='login'),
  path('logout-user', views.logout_user, name='logout'),
  path('regester-user', views.regester_user, name='regester-user'),
]
