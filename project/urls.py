from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('login/', views.loginView),
    path('logout/', views.logoutView),
    path('', views.landingPage),
]
