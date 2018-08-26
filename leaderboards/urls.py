"""Contains URLs for the loaderboards app."""

from django.urls import path
from leaderboards import views


urlpatterns = [
    path(r'', views.home_page_view, name='home'),
]
