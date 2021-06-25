from django.urls import path

from . import views

urlpatterns = [
    path('', views.register, name = 'register'),
    path('<int:login_id>/login/', views.login, name = 'login'),
    path('<int:login_id>/logout/', views.logout, name = 'logout')

]