"""Contains URLs for the loaderboards app."""

from django.contrib.auth import views as auth_views
from django.urls import path
from leaderboards import views


urlpatterns = [
    path(r'', views.Home.as_view(), name='home'),
    path(r'about/', views.About.as_view(), name='about'),
    path(r'categories/', views.CategoryList.as_view(), name='category-list'),
    path(r'categories/<int:pk>/', views.CategoryDetail.as_view(), name='category-detail'),
    path(r'courses/', views.CourseList.as_view(), name='course-list'),
    path(r'courses/<int:course_number>/', views.CourseDetailSixStarLeaderboard.as_view(), name='course-detail'),
    path(r'courses/<int:course_number>/six-star-leaderboard/', views.CourseDetailSixStarLeaderboard.as_view(), name='course-detail-six-star-leaderboard'),
    path(r'courses/<int:course_number>/seven-star-leaderboard/', views.CourseDetailSevenStarLeaderboard.as_view(), name='course-detail-seven-star-leaderboard'),
    path(r'courses/<int:course_number>/six-star-records/', views.CourseDetailSixStarRecords.as_view(), name='course-detail-six-star-records'),
    path(r'courses/<int:course_number>/seven-star-records/', views.CourseDetailSevenStarRecords.as_view(), name='course-detail-seven-star-records'),
    path(r'login/', auth_views.LoginView.as_view(template_name='leaderboards/login.html'), name='login'),
    path(r'logout/', auth_views.LogoutView.as_view(), name='logout'),
]
