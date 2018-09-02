"""Contains URLs for the loaderboards app."""

from django.contrib.auth import views as auth_views
from django.urls import path, reverse_lazy
from leaderboards import views


urlpatterns = [
    path(r'', views.Home.as_view(), name='home'),
    path(r'about/', views.About.as_view(), name='about'),
    path(r'account/edit-profile/', views.ProfileEdit.as_view(), name='account-edit-profile'),
    path(r'account/change-password/', auth_views.PasswordChangeView.as_view(template_name='leaderboards/account_settings_change_password.html', success_url=reverse_lazy('account-edit-profile')), name='account-change-password'),
    path(r'categories/', views.CategoryList.as_view(), name='category-list'),
    path(r'categories/<int:pk>/', views.CategoryDetailLeaderboard.as_view(), name='category-detail'),
    path(r'categories/<int:pk>/leaderboard/', views.CategoryDetailLeaderboard.as_view(), name='category-detail-leaderboard'),
    path(r'categories/<int:pk>/records/', views.CategoryDetailRecords.as_view(), name='category-detail-records'),
    path(r'courses/', views.CourseList.as_view(), name='course-list'),
    path(r'courses/<int:course_number>/', views.CourseDetailSixStarLeaderboard.as_view(), name='course-detail'),
    path(r'courses/<int:course_number>/six-star-leaderboard/', views.CourseDetailSixStarLeaderboard.as_view(), name='course-detail-six-star-leaderboard'),
    path(r'courses/<int:course_number>/seven-star-leaderboard/', views.CourseDetailSevenStarLeaderboard.as_view(), name='course-detail-seven-star-leaderboard'),
    path(r'courses/<int:course_number>/six-star-records/', views.CourseDetailSixStarRecords.as_view(), name='course-detail-six-star-records'),
    path(r'courses/<int:course_number>/seven-star-records/', views.CourseDetailSevenStarRecords.as_view(), name='course-detail-seven-star-records'),
    path(r'login/', auth_views.LoginView.as_view(template_name='leaderboards/login.html'), name='login'),
    path(r'logout/', auth_views.LogoutView.as_view(), name='logout'),
    path(r'submit-record/', views.RecordSubmitHome.as_view(), name='record-submit-home'),
    path(r'submit-record/six-star-course-record/', views.RecordSubmitSixStarCourseRecord.as_view(), name='record-submit-six-star-course-record'),
    path(r'submit-record/seven-star-course-record/', views.RecordSubmitSevenStarCourseRecord.as_view(), name='record-submit-seven-star-course-record'),
    path(r'submit-record/category-record/', views.RecordSubmitCategoryRecord.as_view(), name='record-submit-category-record'),
]
