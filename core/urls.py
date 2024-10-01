from . import views
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('home_view/',views.home_view,name='home_view'),
    path('about_form/',views.about_form,name='about_form'),
    path('education_form/',views.education_form,name='education_form'),
    path('recentwork_form/',views.recentwork_form,name='recentwork_form'),
    
    
]

