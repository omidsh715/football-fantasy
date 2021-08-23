from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView
from . import views

app_name = 'account'

urlpatterns = [
    path('login', LoginView.as_view(template_name='account/login.html', ), name='login'),
    path('logout', LogoutView.as_view(template_name='account/login.html'), name='logout'),
    path('register', views.register, name='register'),
    path('edit', views.edit, name='edit')
]
