"""Views for leaderboards."""

from django.shortcuts import render


def home_page_view(request):
    """View for the main page."""
    return render(request, 'leaderboards/base.html')
