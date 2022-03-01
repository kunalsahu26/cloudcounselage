
from django.urls import path
from . import views
app_name='app'

urlpatterns = [
     
      path('', views.home,name='home'),
      # path('index/login/', views.login_page,name="login"),
      path('index/about/', views.about,name="about"),
      path('index/scope/', views.scope,name="scope"),
      path('register/',views.register_page,name='register'),
      path('index/services/',views.services,name='services'),
      path('index/services/career/',views.career_page,name='career'),
      path('index/services/interview/',views.interview_page,name='interview'),
      path('index/services/cvbuilding/',views.cv_building,name='cvbuilding'),
]