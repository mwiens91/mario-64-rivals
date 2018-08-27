"""Views for leaderboards."""

from django.shortcuts import render
from django.views import View


class HomeView(View):
    """View for the homepage."""
    def get(self, request):
        """Display the homepage."""
        return render(request, 'leaderboards/base.html')
