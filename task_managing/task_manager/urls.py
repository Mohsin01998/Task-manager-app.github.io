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
    path('create_task',views.NewTask,name='create_task'),
    path('view_task',views.ViewTask,name='view_task'),
    path('update_task/<str:pk>/',views.UpdateTask,name='update_task'),
    path('delete_task/<str:pk>/',views.DeleteTask,name='delete_task'),
]
