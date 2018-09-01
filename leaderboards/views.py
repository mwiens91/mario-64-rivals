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


class CourseDetailSixStarLeaderboard(DetailView):
    """A view for viewing six star leaderboards."""
    model = Course
    template_name = "leaderboards/course_detail_six_star_leaderboard.html"
    pk_url_kwarg = "course_number"


class CourseDetailSevenStarLeaderboard(DetailView):
    """A view for viewing seven star leaderboards."""
    model = Course
    template_name = "leaderboards/course_detail_seven_star_leaderboard.html"
    pk_url_kwarg = "course_number"


class CourseDetailSixStarRecords(DetailView):
    """A view for viewing all six star records."""
    model = Course
    template_name = "leaderboards/course_detail_six_star_records.html"
    pk_url_kwarg = "course_number"


class CourseDetailSevenStarRecords(DetailView):
    """A view for viewing all seven star records."""
    model = Course
    template_name = "leaderboards/course_detail_seven_star_records.html"
    pk_url_kwarg = "course_number"
