"""Contains URLs for the loaderboards app."""

from django.contrib.auth import views as auth_views
from django.urls import path
from leaderboards import views


urlpatterns = [
    path(r'', views.Home.as_view(), name='home'),
    path(r'about/', views.About.as_view(), name='about'),
    path(r'courses/', views.CourseList.as_view(), name='course-list'),
    path(r'courses/<int:course_number>/', views.CourseDetail.as_view(), name='course-detail'),
    path(r'login/', auth_views.LoginView.as_view(template_name='leaderboards/login.html'), name='login'),
    path(r'logout/', auth_views.LogoutView.as_view(), name='logout'),
]
