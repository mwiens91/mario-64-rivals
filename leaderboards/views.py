"""Views for leaderboards."""

from django.shortcuts import render
from django.views.generic import DetailView, ListView, TemplateView
from .models import Course


class Home(TemplateView):
    """A view for the homepage."""
    template_name = "leaderboards/home.html"


class About(TemplateView):
    """A view for the about page."""
    template_name = "leaderboards/about.html"


class CourseList(ListView):
    """A view for listing courses."""
    model = Course
    template_name = "leaderboards/course_list.html"


class CourseDetail(DetailView):
    model = Course
    template_name = "leaderboards/course_detail.html"
    pk_url_kwarg = "course_number"
