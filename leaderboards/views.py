"""Views for leaderboards."""

from django.shortcuts import render
from django.views.generic import TemplateView


class HomeView(TemplateView):
    """A view for the homepage."""
    template_name = "leaderboards/base.html"
