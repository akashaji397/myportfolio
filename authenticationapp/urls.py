from . import views
from django.urls import path

urlpatterns = [
    path('register/',views.Register,name='register'),
    path('login/',views.login,name='login'),
    path('home/',views.home,name='home'),
    path('logout/',views.logout,name='logout'),
    path('',views.index,name='index')
]
