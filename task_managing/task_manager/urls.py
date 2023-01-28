from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path("register",views.register,name='register'),
    path('',views.home,name='home'),
    path('login',views.login_page,name='login'),
    path('logout',views.logout_page,name='logout'),
    path('dashboard',views.dashboard,name='dashboard'),
]
