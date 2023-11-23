from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home,name="home"),
    path('login/', views.login_user,name="login"),
    path('logout/', views.logout_user,name="logout"),
    path('register/', views.register_user,name="register"),
    path('customer_records/<int:pk>', views.customer_records,name="records"),
    path('delete_records/<int:pk>', views.delete_record,name="delete"),
    path('update_records/', views.add_record,name="add"),
]
